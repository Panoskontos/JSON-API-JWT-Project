from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    search_fields = ['name', 'id', 'actors','genre']



class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    search_fields = '__all__'
    
