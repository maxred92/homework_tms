from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.GamesList.as_view()),
]