import requests
import json
from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Loading the data via url'

    def add_arguments(self, parser):
        parser.add_argument("json_url", type=str, help="URL of the JSON file")

    def handle(self, *args, **options):
        json_url = options['json_url']
        try:
            response = requests.get(json_url)
            response.raise_for_status()
            place_data = response.json()

            title = place_data.get('title')
            description_short = place_data.get('description_short')
            description_long = place_data.get('description_long')
            longitude = place_data['coordinates'].get('lng')
            latitude = place_data['coordinates'].get('lat')
            image_urls = place_data.get('imgs', [])

            place, created = Place.objects.get_or_create(
                title=title,
                defaults={
                    'place_id': None,
                    'description_short': description_short,
                    'description_long': description_long,
                    'longitude': longitude,
                    'latitude': latitude
                }
            )
            place.title = title
            place.description_short = description_short
            place.description_long = description_long
            place.longitude = longitude
            place.latitude = latitude
            place.save()

            for order, image_url in enumerate(image_urls):

                image_response = requests.get(image_url)
                image_response.raise_for_status()
                image_content = ContentFile(image_response.content)
                image_name = image_url.split('/')[-1]
                image = Image(place=place, order=order)
                image.image.save(image_name, image_content, save=True)
            self.stdout.write(self.style.SUCCESS("Done!"))
        except Exception as e:
            self.stderr.write(self.style.Error(f"Error: {e}"))
