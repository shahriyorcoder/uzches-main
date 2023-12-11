from django.shortcuts import render
from blog import serializers
from rest_framework.generics import  ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filterdjango 
from rest_framework.permissions import AllowAny


class NewsQueryListView(ListAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()

class CourseListView(ListAPIView):
    serializer_class = serializers.CourseSerializer
    queryset = Course.objects.all()
    filter_backends = [filters.SearchFilter,filterdjango.DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['category']
    
class CourseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


class News_Search(ListAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description','content']

class News_Single(RetrieveAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views = obj.views + 1
        obj.save(update_fields=("views", ))
        return super().retrieve(request, *args, **kwargs)
    
