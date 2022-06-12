"""
Serializers for recipe APIs
"""
from core.models import Recipe, Tag
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Recipe detail serializer view"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class TagSerializer(serializers.ModelSerializer):
    """Tag serializer"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']
