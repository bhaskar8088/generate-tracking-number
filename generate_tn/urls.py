from django.urls import path
from .views import TrackingNumberGenerator

urlpatterns = [
    path('generate-tn/', TrackingNumberGenerator.as_view(), name='generate-tn'),
]
