from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Problem, Sign
from .serializers import ProblemSerializer, SignSerializer

# Create your views here.


class ProblemListView(ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class SignListView(ListAPIView):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer

 