from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[

        'GET /api/users',
        'GET /api',

    ]
    return Response(routes)

@api_view(['GET'])
def getUsers(request):
    users=User.objects.all()
    serializer=UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request,pk):
    users=User.objects.get(username=pk)
    serializer=UserSerializer(users)
    return Response(serializer.data)
