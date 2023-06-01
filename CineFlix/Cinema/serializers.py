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
        
class ShowingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    tickets_sold = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Showing
        fields = ["id","url","screen","film","showing_date","showing_time","tickets_sold"]