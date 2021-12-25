from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import InventorySerializer
from .models import Inventory

# Create your views here.
def main(request):
    return HttpResponse("Hello")

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        'api/token/refresh',
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getInventory(request):
    user = request.user
    inventory = user.inventory_set.all()
    serializers = InventorySerializer(inventory, many=True)
    return Response(serializers.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer