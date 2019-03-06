# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from distutils.version import LooseVersion
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from cms import __version__ as cms_version
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models, forms, filters


CMS_GTE_330 = LooseVersion(cms_version) >= LooseVersion('3.3.0')


class AdjustableCacheMixin(object):
    """
    For django CMS < 3.3.0 installations, we have no choice but to disable the
    cache where there is time-sensitive information. However, in later CMS
    versions, we can configure it with `get_cache_expiration()`.
    """
    if not CMS_GTE_330:
        cache = False

    def get_cache_expiration(self, request, instance, placeholder):
        return getattr(instance, 'cache_duration', 0)

    def get_fieldsets(self, request, obj=None):
        """
        Removes the cache_duration field from the displayed form if we're not
        using django CMS v3.3.0 or later.
        """
        fieldsets = super(AdjustableCacheMixin, self).get_fieldsets(request, obj=None)
        if CMS_GTE_330:
            return fieldsets

        field = 'cache_duration'
        for fieldset in fieldsets:
            new_fieldset = [
                item for item in fieldset[1]['fields'] if item != field]
            fieldset[1]['fields'] = tuple(new_fieldset)
        return fieldsets


@plugin_pool.register_plugin
class EventRelatedPlugin(AdjustableCacheMixin, CMSPluginBase):
    module = 'JumpSuite Events'
    TEMPLATE_NAME = 'js_events/plugins/related_events__%s.html'
    name = _('Related Events')
    model = models.EventRelatedPlugin
    form = forms.EventRelatedPluginForm
    render_template = TEMPLATE_NAME % forms.LAYOUT_CHOICES[0][0]

    def get_event(self, request):
        if request and request.resolver_match:
            view_name = request.resolver_match.view_name
            namespace = request.resolver_match.namespace
            if view_name == '{0}:event-detail'.format(namespace):
                event = models.Event.objects.active_translations(
                    slug=request.resolver_match.kwargs['slug'])
                if event.count() == 1:
                    return event[0]
        return None

    def render(self, context, instance, placeholder):
        request = context.get('request')
        context['instance'] = instance

        context['title'] = instance.title
        context['icon'] = instance.icon
        context['image'] = instance.image
        related_types = instance.related_types
        related_hosts = instance.related_hosts.all()
        related_categories = instance.related_categories.all()
        related_services = instance.related_services.all()

        qs = models.Event.objects.published().distinct()
        if related_types.exists():
            qs = qs.filter(app_config__in=related_types.all())
        if related_hosts:
            qs = qs.filter(host__in=related_hosts.all())
        if related_categories:
            qs = qs.filter(categories__in=related_categories.all())
        if related_services:
            qs = qs.filter(services__in=related_services.all())
        if instance.exclude_current_item:
            current_event = self.get_event(request)
            if current_event is not None:
                qs = qs.exclude(id=current_event.id)
        if instance.featured:
            qs = qs.filter(is_featured=True)
        if instance.time_period == 'future':
            qs = qs.filter(event_start__gt=now())
        elif instance.time_period == 'past':
            qs = qs.filter(event_start__lte=now())

        if instance.layout == 'filter':
            f = filters.EventFilters(request.GET, queryset=qs)
            context['filter'] = f
            qs = f.qs

        context['related_events'] = qs[:int(instance.number_of_items)]
        return context

    def get_render_template(self, context, instance, placeholder):
        return self.TEMPLATE_NAME % instance.layout
