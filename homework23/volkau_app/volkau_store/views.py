from django.shortcuts import get_object_or_404, render
from volkau_store.models import Games, Category
from django.http import HttpRequest
# Create your views here.



def game(request, game_slug):
    game = get_object_or_404(Games, slug=game_slug)
    context = {
        'game' : game
    }
    return render(request, 'store/game.html', context)

def sorting_game(request: HttpRequest, sort_by):
    dict = {
        'price': Games.objects.filter(is_active=True).order_by('-price').all(),
        'name': Games.objects.filter(is_active=True).order_by('name').all()
    }
    games = dict.get(sort_by)
    context = {
        'category' : category,
        'games' : games
    }
    return render(request, 'store/index.html', context)

def all_games(request):
    games = Games.objects.filter(is_active=True).all()
    return render(request, 'store/index.html', {'games': games})


def category(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    games_category = Games.objects.filter(is_active=True, category=category).all()
    context = {
        'category' : category,
        'games_category' : games_category
    }
    return render(request, 'store/category.html', context)


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})

