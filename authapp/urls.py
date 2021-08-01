from django.urls import path
from authapp.views import TestView


urlpatterns = [
    path('test/', TestView.as_view())
]
