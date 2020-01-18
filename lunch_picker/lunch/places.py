import requests, json
from django.conf import settings


def get_restaurants():
  api_key = settings.GOOGLE_MAPS_API_KEY

  url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurant&key='

  url += api_key

  res = requests.get(url)

  place_json = res.json()['results']

  name_list = []
  for i in range(len(place_json)):
    name_list.append(place_json[i]['name'])

  return name_list
