from django.http import HttpResponse
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
def index(request):
    return HttpResponse("Hello, world. You're at the destinations index.")




class DestinationList(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationDTO

