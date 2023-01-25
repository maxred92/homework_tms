from django.urls import path
from . import views


urlpatterns = [
    path('factorial/', views.factorial_func, name='factorial'),
    path ('kanyewestquotes/', views.KanyeWestView.as_view(), name='kanyewestquotes'),
    path('kanyewestquotes/<quotes>/', views.KanyeWestView.as_view(), name='kanyewestquotes')
]