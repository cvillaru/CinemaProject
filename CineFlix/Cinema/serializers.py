from rest_framework import serializers
from Cinema.models import *


class FilmSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Film
        fields = ["id","url","title","description"]
        
        
class ScreenSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Screen
        fields = ["id","url","screen_number","capacity"]