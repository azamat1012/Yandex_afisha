from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=150, unique=True, null=True,
                             blank=False, verbose_name="Название места")
    short_description = models.TextField(
        verbose_name="Короткое описание места", null=True, blank=True)
    long_description = HTMLField(
        verbose_name="Подробное описание места", null=True, blank=True)
    longitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Широта")

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='images', verbose_name="Картинки")
    image = models.ImageField(upload_to='images/', verbose_name="Картинка")
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.place.title
