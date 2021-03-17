from django.contrib import admin

# Register your models here.
from .models import Book, Author, Publisher, Genre, GenreSub, Country


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(GenreSub)
admin.site.register(Country)