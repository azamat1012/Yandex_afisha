from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Image
import json
from django.http.response import JsonResponse
from django.urls import reverse


def fetch_places_data(request):
    places = Place.objects.all()

    geojson_container = {
        'type': 'FeatureCollection',
        'features': []
    }

    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.place_id,
                'detailsUrl': reverse('place_detail', args=[place.id])
            }
        }
        geojson_container['features'].append(feature)

    geojson_data = json.dumps(geojson_container)
    context = {'geojson_data': geojson_data}
    return render(request, 'index.html', context=context)


def place_detail(request, id):
    place = get_object_or_404(Place, id=id)
    images = place.images.all()

    places_data = {
        'title': place.title,
        'imgs': [img.image.url for img in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }

    return JsonResponse(places_data, json_dumps_params={'ensure_ascii': False, 'indent': 2})
