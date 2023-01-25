from django.shortcuts import render
from volkau_store.models import Games, Category
from django.shortcuts import get_object_or_404
# Create your views here.



def game(request, game_slug):
    game = get_object_or_404(Games, slug=game_slug)
    context = {
        'game' : game
    }
    return render(request, 'store/game.html', context)

def sorting_game(request, sort_by):
    sort_by_cat = Games.objects.filter(is_active=True).all()
    sort_dict = {
        'name' : sort_by_cat.order_by('name'),
        'price': sort_by_cat.order_by('price')
    }
    games = sort_dict.get(sort_by)
    return render(request, 'store/game.html', {'games': games})

def all_games(request):
    games = Games.objects.filter(is_active=True).all()
    return render(request, 'store/index.html', {'games': games})


def category(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    games = Games.objects.filter(is_active=True, category=category)
    context = {
        'category' : category,
        'games' : games
    }
    return render(request, 'store/category.html', context)


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})

