from APIs.models import Category
import json
from rest_framework import serializers
class category_list(serializers.ListSerializer):
    def create(self, validated_data):
        items= [Category(**item) for item in validated_data]
        return Category.objects.bulk_create(items)
class category_serializing(serializers.Serializer):
    category=serializers.CharField()
    name=serializers.CharField()
    author=serializers.CharField()
    title=serializers.CharField()
    description=serializers.CharField()
    published=serializers.DateTimeField()
    urlToImage=serializers.CharField()
    class Meta:
        list_serializer_class = category_list

class news_serializing(serializers.Serializer):
    category=serializers.CharField()
    name=serializers.CharField()
    author=serializers.CharField()
    title=serializers.CharField()
    description=serializers.CharField()
    published=serializers.DateTimeField()
    urlToImage=serializers.CharField()
    