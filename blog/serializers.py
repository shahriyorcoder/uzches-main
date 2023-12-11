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
