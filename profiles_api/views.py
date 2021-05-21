from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """Returns a list of APIVIew features"""
        an_apiview = [
            'Uses HTTP methods as function (get post patch put delete)',
            'is similiar to a traditional django view',
            'gives you the most control over application logic',
            'Gives the most control over app logic',
            'is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
