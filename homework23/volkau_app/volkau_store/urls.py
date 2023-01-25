from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.all_games, name='games'),
    path('category/', views.all_categories, name='all_categories'),
    path('<slug:game_slug>/', views.game, name='game_slug'),
    path('category/<slug:category_slug>/', views.category, name='games_category')
]