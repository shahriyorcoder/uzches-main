from rest_framework import serializers

from blog import  models
class NewsSerializer(serializers.ModelSerializer):
    views = serializers.SerializerMethodField()

    class Meta:
        model = models.News
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.views += 1
        instance.save()
        return instance
    
    def get_views(self, obj):
        return obj.views
