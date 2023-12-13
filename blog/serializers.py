from rest_framework import serializers

from blog import  models


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.News
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Module
        fields = "__all__"

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = "__all__"
