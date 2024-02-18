from rest_framework import serializers

from ..models import Data


class ModelSerializer(serializers.ModelSerializer):
    class  Meta :
        model =Data
        fields = ['donnée']