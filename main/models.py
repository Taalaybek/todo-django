from django.db import models

class ToDo(models.Model):
  title = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  is_favorite = models.BooleanField(default=False)
  is_done = models.BooleanField(default=False)

class Book(models.Model):
  title = models.CharField(max_length=255)
  subtitle = models.CharField(max_length=200)
  description = models.TextField(null=True)
  price = models.IntegerField(null=True)
  genre = models.CharField(max_length=150)
  author = models.CharField(max_length=255)
  year = models.DateField(auto_now_add=False)
  date = models.DateField(auto_now_add=True)
  is_favorite = models.BooleanField(default=False)
