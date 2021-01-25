from django.shortcuts import render, HttpResponse
from .models import ToDo

# Create your views here.
def homepage(request):
  todos = ToDo.objects.all()
  return render(request, "index.html", {"todos": todos})