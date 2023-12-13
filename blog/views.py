# from django.shortcuts import render
from blog import serializers
from rest_framework.generics import  ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.decorators import api_view
from .models import *
from rest_framework import filters
from django_filters import rest_framework as filterdjango 
from rest_framework.response import Response

# from rest_framework.permissions import AllowAny

def trigger_error(request):
    division_by_zero = 1 / 0

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

    def retrieve(self, request, *args, **kwargs):
        course = self.get_object()
        comments = course.comment.all()
        lesson= course.lessons.all()
        serializer_course = self.get_serializer(course)
        serializer_lesson = serializers.LessonSerializer(lesson, many=True)
        serializer_comment = serializers.CommentSerializer(comments, many=True)
        serializer_course = self.get_serializer(course)

        response_data = {
            'course': serializer_course.data,
            'lesson': serializer_lesson.data,
            'comment': serializer_comment.data,
        }
        return Response(response_data)


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
    
