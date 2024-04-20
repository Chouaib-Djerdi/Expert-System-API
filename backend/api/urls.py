from django.urls import path
from .views import ProblemListView, SignListView, DiagnosisView, SingleSignView

urlpatterns = [
    path("problems/", ProblemListView.as_view(), name="problems-list"),
    path("signs/", SignListView.as_view(), name="signs-list"),
    path("diagnosis/", DiagnosisView.as_view(), name="diagnosis"),
    path("sign/", SingleSignView.as_view(), name="single-sign"),
]
