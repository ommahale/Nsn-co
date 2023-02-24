from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,WorksSerializer,ArtistSerializer
from .models import Work,Artist
from rest_framework import permissions
# Create your views here.


class RegisterAPI(generics.CreateAPIView):
    serializer_class=UserSerializer
    queryset=get_user_model()
    permission_classes=[permissions.AllowAny]

class WorksAPI(generics.ListAPIView):
    serializer_class=WorksSerializer
    queryset=Work.objects.all()
    def get_queryset(self):
        work_type=self.request.query_params.get('work_type',None)
        artist=self.request.query_params.get('artist',None)
        if work_type:
            return Work.objects.filter(work_type=work_type)
        if artist:
            artist_obj=Artist.objects.get(name=artist)
            return Work.objects.filter(artist__in=[artist_obj])
        return Work.objects.all()
