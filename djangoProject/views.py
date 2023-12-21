from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Greeting
from .serializers import GreetingSerializer


class GreetingView(APIView):
    def get(self, request):
        greeting = Greeting.objects.first()
        serializer = GreetingSerializer(greeting)
        return Response(serializer.data, status=status.HTTP_200_OK)
