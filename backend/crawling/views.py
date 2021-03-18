from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView

from . import crawling

def test(request):
    crawling.crawlingTest()
    return HttpResponse("aa")