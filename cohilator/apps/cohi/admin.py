from django.contrib.admin import ModelAdmin, register

from cohilator.apps.cohi.models import Brew, BrewType, Country, Producer, Roaster, Package, Grinder, Technique


@register(BrewType)
class BrewTypeAdmin(ModelAdmin):
    pass


@register(Country)
class CountryAdmin(ModelAdmin):
    pass


@register(Producer)
class ProducerAdmin(ModelAdmin):
    pass


@register(Roaster)
class RoasterAdmin(ModelAdmin):
    pass


@register(Package)
class PackageAdmin(ModelAdmin):
    pass


@register(Grinder)
class GrinderAdmin(ModelAdmin):
    pass


@register(Technique)
class TechniqueAdmin(ModelAdmin):
    pass


@register(Brew)
class BrewAdmin(ModelAdmin):
    list_display = ['package', 'type', 'technique', 'rating']
    list_filter = ['type__name', 'technique__name', 'package__name', 'rating']
