from django.contrib import admin
from doors import models
from doors import forms


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FrameMaterial)
class FrameMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CoverMaterial)
class CoverMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Height)
class HeightAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Width)
class WidthAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PackingMaterial)
class PackingMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    form = forms.ColorModelForm


@admin.register(models.Picture)
class PictureAdmin(admin.ModelAdmin):
    pass


class PictureInline(admin.TabularInline):
    model = models.Picture


@admin.register(models.Door)
class DoorAdmin(admin.ModelAdmin):
    inlines = [PictureInline]
