from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


from . import serializers

class HelloApiView(APIView):
    """ API View de prueba """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Retorna una lista de caracteristicas del APIView """
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuestra aplicación',
            'Esta mapeado manualmente a los URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Actualiza un objeto """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Maneja actualizacion parcial de un objeto """
        return Response({'method': 'PATCH'})
        
    def delete(self, request, pk=None):
        """ Elimina un objeto """
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """ Test API View Set """
    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """ Retornar mensaje """

        a_viewset = [
            'Usa acciones (list, create, retrieve, update, parcial_update, destroy)',
            'Automaticamente mapea a los URLs usando Routers',
            'Provee mas funcionalidades con menos codigo'
        ]

        return Response({'message': 'Hola!', 'a_viewset': a_viewset})

    def create(self, request):
        """ Crear nuevo mensaje """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer._validated_data.get('name')
            message = f'Hola {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Obtiene un objeto y su ID """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Actualiza un objeto """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Actualiza parcialmente un objeto """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Elimina un objeto """
        return Response({'http_method': 'DELETE'})

