import json
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# book/
class BookListAPIView(APIView):
    # def get(self, request):
    #     return

    def post(self, request):        
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=201)
        else:
            return Response(data = serializer.errors, status = 400)

# book/id/<int:id>/
class BookDetailAPIView(APIView):
    def get(self, request, id):
        # book = Book.objects.get(pk = id)
        book = get_object_or_404(Book, pk = id)
        bookJson = BookSerializer(book).data

        returnJson = {
            'book' : bookJson
        }
        # return JsonResponse(returnJson)
        return Response(data = returnJson)

    def put(self, request, id):
        book = Book.objects.get(pk = id)
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(data = serializer.errors, status = 400)

    def delete(self, request, id):
        # 작동안함
        book = Book.objects.get(pk = id)
        book.delete()
        # print("디버깅 삭제 확인", id)
        return Response(status = status.HTTP_204_NO_CONTENT)

# book/string/
class BookStringListAPIView(APIView):
    def get(self, request):
        try:
            bookTitle = request.data["title"]
            book = Book.objects.filter(title = bookTitle)
            bookJson = BookSerializer(book, many = True).data
            return Response(data = bookJson)
        except:
            json = {
                "title": [
                    "This field is required."
                ]
            }
            return Response(data = json, status = 400)
        
    def post(self, request):
        # 작가이름을 작가번호로 변경
        if request.data.get('author') != None:
            for i in range(len(request.data.get('author'))):
                authorName = request.data.get('author')[i]
                authors = Author.objects.filter(name = authorName)
                if len(authors) != 0:
                    request.data['author'][i] = authors[0].id
                else:
                    json = {
                        "author" : [ "Could not find author " + authorName]
                    }
                    return Response(data = json, status = 400)

        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = 201)
        else:
            return Response(data = serializer.errors, status = 400)

# book/string/<int:id>
class BookStringDetailAPIView(APIView):
    def get(self, request, id):
        # book = Book.objects.get(pk = id)
        book = get_object_or_404(Book, pk = id)
        bookJson = BookSerializer(book).data

        # 작가번호를 작가이름으로 변경
        for i in range(len(bookJson['author'])):
            print("test")
            authorName = Author.objects.get(pk = bookJson['author'][i]).name
            bookJson['author'][i] = authorName

        returnJson = {
            'book' : bookJson
        }
        # return JsonResponse(returnJson)
        return Response(data = returnJson)



# author/
class AuthorListAPIView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=201)
        else:
            return Response(data = serializer.errors, status = 400)

# author/id/<int:id>/
class AuthorDetailAPIView(APIView):
    def get(self, request, id):
        author = get_object_or_404(Author, pk = id)
        authorJson = AuthorSerializer(author).data
        return Response(data = {'author' : authorJson})

    def put(self, request, id):
        author = Author.objects.get(pk = id)
        serializer = AuthorSerializer(author, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data = serializer.errors, status = 400)

# author/string/
class AuthorStringListAPIView(APIView):
    def get(self, request):
        serializer = AuthorSerializer(data = request.data)
        print(request.data)
        if serializer.is_valid():
            author = Author.objects.filter(name = serializer.data.get('name'))
            authorJson = AuthorSerializer(author, many = True).data
            return Response(data = authorJson)
        else:
            return Response(data = serializer.errors, status = 400)
