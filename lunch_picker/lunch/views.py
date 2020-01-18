from django.shortcuts import render
from django.http import HttpResponse
from .places import get_restaurants

def index(request):
  return render(request, 'lunch/index.html')

def register(request):
  return HttpResponse("You've landed on the register page.")

def login(request):
  return HttpResponse("You've landed on the log in page.")

def places(request):
  if request.method == "POST":
    try:
      price = request.POST['price']
      location = request.POST['location']
      rating = request.POST['rating']
      cuisine = request.POST['cuisine']
    except KeyError: # Checks if user has selected all fields
      return render(request, 'lunch/places.html', {
        'price': '',
        'location': '',
        'rating': '',
        'cuisine': '',
        'name_list': '',
        'error_msg': "You didn't select something.",
      })

    # Call places.py and searches 'restaurant' and then returns info based on user parameters
    name_list = get_restaurants()

    return render(request, 'lunch/places.html', {
      'price': price,
      'location': location,
      'rating': rating,
      'cuisine': cuisine,
      'name_list': name_list,
      'error_msg': '',
    })
  else:
    return "not a POST request."
