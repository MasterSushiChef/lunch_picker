from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'lunch/index.html')

def register(request):
  return HttpResponse("You've landed on the register page.")

def login(request):
  return HttpResponse("You've landed on the log in page.")

def places(request):
  return HttpResponse("You've landed on the results page.")
