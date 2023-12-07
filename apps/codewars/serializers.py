from rest_framework import serializers
from .models import Chellanger, CodewarsGroup, Chellange


class ChellangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chellanger
        fields = "__all__"


class CodewarsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodewarsGroup
        fields = "__all__"


class ChellangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chellange
        fields = "__all__"
        