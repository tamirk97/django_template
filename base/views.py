from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(req):
    return Response('hello')

# def index(req):
#     return JsonResponse('hello', safe=False)

def test(req):
    return JsonResponse({'hello': 'world'}, safe=False)