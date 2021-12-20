from rest_framework.views import APIView

from rest_framework.response import Response


class HelloApiView(APIView):
    """ API View de prueba """

    def get(self, request, format=None):
        """ Retorna una lista de caracteristicas del APIView """
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuestra aplicación',
            'Esta mapeado manualmente a los URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})