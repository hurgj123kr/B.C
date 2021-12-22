
from django.urls import path
from .views import ChocoPrediction

urlpatterns = [
    path('choco/', ChocoPrediction.as_view(), name = 'choco_prediction'),
]