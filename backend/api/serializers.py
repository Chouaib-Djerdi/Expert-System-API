from rest_framework import serializers
from .models import Problem, Sign


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"


class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = "__all__"
