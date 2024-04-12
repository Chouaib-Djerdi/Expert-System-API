from rest_framework import serializers
from .models import Problem, Sign


class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = "__all__"


class ProblemSerializer(serializers.ModelSerializer):
    signs = SignSerializer(many=True, read_only=True)

    class Meta:
        model = Problem
        fields = "__all__"


class DiagnosisSerializer(serializers.Serializer):
    signs = serializers.ListField(child=serializers.CharField())
