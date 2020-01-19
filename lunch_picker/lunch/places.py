import requests, json
from django.conf import settings


# Very inaccurate since it find location using IP, not used
"""
def get_user_location():
  try:
    g = geocoder.ip('me')
  except ConnectionError:
    return "Cannot connect to server."

  if g.ok is False:
    return "No result found for query."
  else:
    return g.latlng
"""

# Pull list of restaurant names, ratings, number of reviews, price level
# Make radius based on form input, add rating and price level param
def get_restaurants(lat, lng):
  api_key = settings.GOOGLE_MAPS_API_KEY

  url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
  url += 'radius=5000&keyword=restaurant'
  url += ('&location=' + str(lat) + ',' + str(lng))
  url += ('&key=' + api_key)

  res = requests.get(url)

  place_json = res.json()['results']

  name_list = []
  for i in range(len(place_json)):
    name_list.append(place_json[i]['name'])

  return name_list
