from .models import Place, Image

from django.contrib import admin
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image
    extra = 10
    readonly_fields = ['image_preview']
    raw_id_fields = ['place']

    def image_preview(self, obj):
        try:
            return format_html(
                '<img src="{}" width="auto" height="200px" />',
                obj.image.url
            )
        except Exception:
            return "Фото отсутствует"



@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]




@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'place']
    search_fields = ['place__title']
    raw_id_fields = ['place']

    def image_preview(self, obj):
        try:
            return format_html(
                '<img src="{}" width="auto" height="200px" />',
                obj.image.url
            )
        except Exception:
            return "Фото отсутствует"
