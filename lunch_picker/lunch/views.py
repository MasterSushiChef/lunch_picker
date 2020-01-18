from django.shortcuts import render
from django.http import HttpResponse

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
        'error_msg': "You didn't select something."
      })

    # Call places.py and searches 'restaurant' and then returns info based on user parameters

  return render(request, 'lunch/places.html', {
    'price': price,
    'location': location,
    'rating': rating,
    'cuisine': cuisine,
    'error_msg': '',
  })
