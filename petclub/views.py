from django.shortcuts import render

# Create your views here.

# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio

class Pets(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Esto es un get", status=200) # respuesta del servicio

    def post(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Esto es un post", status=200) # respuesta del servicio

    def patch(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Esto es un patch", status=200) # respuesta del servicio
    def delete(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Esto es un delete", status=200) # respuesta del servicio

class Persons(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Esto es un get", status=200) # respuesta del servicio

    def post(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Esto es un post", status=200) # respuesta del servicio

    def patch(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Esto es un patch", status=200) # respuesta del servicio
    def delete(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Esto es un delete", status=200) # respuesta del servicio