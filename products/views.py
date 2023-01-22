from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    return HttpResponse('Hello World')


def newProd(request):
    return HttpResponse('New Products')


