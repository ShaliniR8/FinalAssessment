from django.shortcuts import render, get_object_or_404
from .models import Character
# Create your views here.
def home_view(request, *args, **kwargs):
     return render(request, 'home.html')

def char_view(request, *args, id):
     obj = get_object_or_404( Character, id=id)
     context = {
          'obj' : obj
     }
     return render(request, 'home.html', context)