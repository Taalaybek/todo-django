from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book

# Create your views here.
def homepage(request):
  todos = ToDo.objects.all()
  return render(request, "index.html", {"todos": todos})

def books(request):
  books = Book.objects.all()
  return render(request, "books.html", {"books": books})

def add_todo(request):
  todo = ToDo(title=request.POST['title'])
  todo.save()
  return redirect(homepage)

def add_book(request):
  title = request.POST['title']
  subtitle = request.POST['subtitle']
  date = request.POST['date']
  author = request.POST['author']
  genre = request.POST['genre']
  description = request.POST['description']
  price = request.POST['price']
  Book(title=title, subtitle=subtitle, year=date, genre=genre, author=author, description=description, price=price).save()
  return redirect(books)

def delete_todo(request, id):
  todo = ToDo.objects.get(id=id)
  todo.delete()
  return redirect(homepage)

def mark_todo(request, id):
  todo = ToDo.objects.get(id=id)

  if (todo.is_favorite):
    todo.is_favorite = False
  else:
    todo.is_favorite = True
  
  todo.save()
  return redirect(homepage)

def make_done(request, id):
  todo = ToDo.objects.get(id=id)

  if todo.is_done:
    todo.is_done = False
  else:
    todo.is_done = True
    if todo.is_favorite:
      todo.is_favorite = False

  todo.save()

  return redirect(homepage)