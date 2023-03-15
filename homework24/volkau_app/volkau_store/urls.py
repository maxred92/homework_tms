from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.all_categories, name='all_categories'),
    path('<slug:game_slug>/',views.game, name='game_slug'), 
    path('category/<slug:category_slug>/', views.category, name='games_category'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('search', views.search, name='search'),
]