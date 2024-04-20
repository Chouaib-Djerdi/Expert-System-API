from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Problem, Sign
from .serializers import ProblemSerializer, SignSerializer, DiagnosisSerializer
from .utils import diagnose_problem

# Create your views here.


class ProblemListView(ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class SignListView(ListAPIView):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer


class DiagnosisView(APIView):
    def post(self, request):
        serializer = DiagnosisSerializer(data=request.data)
        if serializer.is_valid():
            signs = serializer.validated_data["signs"]
            possible_problem = diagnose_problem(signs)
            problem = Problem.objects.get(name=possible_problem)
            serializer = ProblemSerializer(problem)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
