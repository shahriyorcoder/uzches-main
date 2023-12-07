from django.shortcuts import render
from blog import serializers
from rest_framework.generics import  ListAPIView,RetrieveAPIView
from rest_framework.decorators import api_view
from .models import *
from rest_framework import viewsets
from rest_framework import filters


class BookQueryListView(ListAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()

    # def get_queryset(self):
    #     top_books = News.objects.all()
    #     return top_books


class Book_Search(ListAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description','content']



class Book_Single(RetrieveAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()

    # def get_queryset(self):
    #     top_books = News.objects.all()
    #     return top_books