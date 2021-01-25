from django.shortcuts import render, HttpResponse
from .models import ToDo, Book

# Create your views here.
def homepage(request):
  todos = ToDo.objects.all()
  return render(request, "index.html", {"todos": todos})

def books(request):
  books = Book.objects.all()
  return render(request, "books.html", {"books": books})