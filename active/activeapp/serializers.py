from rest_framework import serializers
from . models import Sliders , Homedata

class SlidersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sliders
        fields='__all__'
class Slidersallserializer(serializers.ModelSerializer):
    class Meta:
        model=Sliders
        fields='__all__'
class Homedataserializers(serializers.ModelSerializer):
    class Meta:
        model=Homedata
        fields="__all__"