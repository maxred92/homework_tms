from django.urls import path,re_path, reverse
from . import views

urlpatterns = [
    path('', views.index, name='class_view'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name ='skills'),
    path('aboutme/', views.aboutme, name='aboutme')

]