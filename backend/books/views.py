from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .models import Book
import json
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer

class BookAPI(View):
    def get(self, request, id):
        book = Book.objects.get(book_number = id)
        bookJson = BookSerializer(book).data
        return JsonResponse({'book' : bookJson})

    def post(self, request, id):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            newBook = Book(title = request['title'],
                           ISBN = request['ISBN'])
        else:
            newBook = Book(title = request.POST['title'],
                           ISBN = request.POST['ISBN'])
        newBook.save()
        return HttpResponse(status=200)

    def put(self, request, id):
        return

    def delete(self, request, id):
        book = Book.objects.get(book_number = id)
        book.delete()
        return HttpResponse(status=200)
    