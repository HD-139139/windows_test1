from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("어서와 장고는 처음이지?")
# Create your views here.
