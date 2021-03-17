import json
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class BookDetailAPIView(APIView):
    def get(self, request, id):
        # book = Book.objects.get(book_number = id)
        book = get_object_or_404(Book, book_number = id)
        bookJson = BookSerializer(book).data
        returnJson = {
            'book' : bookJson
        }
        # return JsonResponse(returnJson)
        return Response(data = returnJson)

    def put(self, request, id):
        book = Book.objects.get(book_number = id)
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(data = serializer.errors, status = 400)

    def delete(self, request, id):
        # 작동안함
        book = Book.objects.get(book_number = id)
        book.delete()
        # print("디버깅 삭제 확인", id)
        return Response(status = status.HTTP_204_NO_CONTENT)

class BookListAPIView(APIView):
    def get(self, request):
        return

    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=201)
        else:
            return Response(data = serializer.errors, status = 400)

class AuthorDetailAPIView(APIView):
    def get(self, request, id):
        author = get_object_or_404(Author, author_number = id)
        authorJson = AuthorSerializer(author).data
        return Response(data = {'author' : authorJson})

    def put(self, request, id):
        author = Author.objects.get(author_number = id)
        serializer = AuthorSerializer(author, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data = serializer.errors, status = 400)

class AuthorListAPIView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=201)
        else:
            return Response(data = serializer.errors, status = 400)

class AuthorSearchAPIView(APIView):
    def get(self, request):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            author = Author.objects.filter(name = serializer.data.get('name'))
            authorJson = AuthorSerializer(author, many = True).data
            return Response(data = authorJson)
        else:
            return Response(data = serializer.errors, status = 400)
