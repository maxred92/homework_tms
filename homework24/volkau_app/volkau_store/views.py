from django.shortcuts import get_object_or_404, render
from volkau_store.models import Games, Category
from django.http import HttpRequest
from django.core.paginator import Paginator
# Create your views here.



def game(request, game_slug):
    game = get_object_or_404(Games, slug=game_slug)
    context = {
        'game' : game
    }
    return render(request, 'store/game.html', context)

def index(request: HttpRequest):
    sort = request.GET.get('order_by')
    field, direction = '', ''

    games = Games.objects.filter(is_active=True)
    if sort:
        field, direction = sort.split(':')
        flow = '' if direction == 'asc'else '-'
        sorting = f'{flow}{field}'
        games = games.order_by(sorting)
    paginator = Paginator(games, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'field' : field,
        'direction' : direction,
        'page_obj' : page_obj
    }
    return render(request, 'store/index.html', context)

# def all_games(request):
#     games = Games.objects.filter(is_active=True).all()
#     return render(request, 'store/index.html', {'games': games})


def category(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    #games_category = Games.objects.filter(is_active=True, category=category).all()
    games_category = category.games_set.filter(is_active=True)
    context = {
        'category' : category,
        'games_category' : games_category
    }
    return render(request, 'store/category.html', context)


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})

