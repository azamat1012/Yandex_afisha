from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline


class ImageInline(SortableTabularInline):
    model = Image
    extra = 10
    readonly_fields = ['image_preview']

    def image_preview(self, obj):

        try:
            return format_html(
                '<img src="{url}" width="auto;" height="200px" />'.format(
                    url=obj.image.url,
                    width=obj.image.width,
                    height=obj.image.height,
                )
            )
        except Exception as e:
            return ("Фото отсутствует")


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ImageInline]
