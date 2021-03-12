from django.contrib import admin

# Register your models here.
from .models import Book, Author, Publisher, Genre, Country


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Country)