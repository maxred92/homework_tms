from django.urls import path, re_path
from . import views

urlpatterns = [
    path('games/', views.GamesList.as_view()),
    re_path('^games/(?P<category>.+)/$', views.GetCategoryGameInfoView.as_view()),
    path('filter-games/', views.GetGameInfoFilterView.as_view()),
    path('search-games/', views.GetGameInfoSearchView.as_view()),
    path('order-games/', views.GetGameInfoOrderView.as_view())

]