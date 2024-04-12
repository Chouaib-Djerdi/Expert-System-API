from django.urls import path
from .views import ProblemListView, SignListView

urlpatterns = [
    path("problems/", ProblemListView.as_view(), name="problems-list"),
    path("signs/", SignListView.as_view(), name="signs-list"),
]
