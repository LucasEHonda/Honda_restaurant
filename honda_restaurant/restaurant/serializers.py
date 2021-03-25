from rest_framework import serializers
from .models import Cooker, Recipe

# Serializers define the API representation.
class CookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooker
        fields = '__all__'
        depth = 1

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        depth = 1

