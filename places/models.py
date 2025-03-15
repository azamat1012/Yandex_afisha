from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    place_id = models.CharField(max_length=100, null=True, unique=True)
    title = models.CharField(max_length=150,null=True, unique=True)
    description_short = models.TextField()
    description_long = HTMLField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Image(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(
        upload_to='images/', default='none', verbose_name="Картинка")
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.place.title

    class Meta:
        ordering = ['order']
