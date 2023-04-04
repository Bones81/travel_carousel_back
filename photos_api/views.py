from django.shortcuts import render
from rest_framework import generics
from .serializers import PhotoSerializer
from .models import Photo

# Create your views here.

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all().order_by('id')
    serializer_class = PhotoSerializer

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all().order_by('id')
    serializer_class = PhotoSerializer
