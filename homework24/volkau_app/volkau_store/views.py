from django.shortcuts import get_object_or_404, render
from volkau_store.models import Games, Category, Comment
from .forms import CommentForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.http import HttpRequest, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from better_profanity import profanity
from volkau_store.tasks import log_store
from django.core import serializers


from datetime import datetime, timedelta

# Create your views here.



# @login_required(login_url=reverse_lazy('users:login'))
def game(request, game_slug):
    game = get_object_or_404(Games, slug=game_slug)
    last_visited = request.COOKIES.get(game_slug + '_lasttime')
    views_number = int(request.COOKIES.get(game_slug + '_viewsnumbers', 0))
    average_rating = game.comments.aggregate(Avg('rating'))
    average_rating = average_rating['rating__avg']
    comments = game.comments.all().order_by('-created') 
    new_comment = None  
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)  
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.game = game  
            new_comment.save() 
            
 
    else:  
        comment_form = CommentForm()
    context = {
        'game': game,  
		'comments': comments,  
		'new_comment': new_comment,  
		'comment_form': comment_form,
        'average_rating': average_rating,
        'last_visited': last_visited,
        'views_number': views_number
    } 
    response = render(request,  'store/game.html', context)
    visit_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response.set_cookie(game_slug + '_lasttime', visit_time, max_age=timedelta(days=20))
    response.set_cookie(game_slug + '_viewsnumbers', views_number+1, max_age=timedelta(days=20))
    log_store.delay(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(request.path), str(request.user))
    return response




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

@login_required(login_url='users:login', redirect_field_name='next')
def category(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    #games_category = Games.objects.filter(is_active=True, category=category).all()
    games_category = category.games_set.filter(is_active=True)
    log_store.delay(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(request.path), str(request.user))

    context = {
        'category' : category,
        'games_category' : games_category
    }
    return render(request, 'store/category.html', context)


def all_categories(request):
    categories = Category.objects.all()
    log_store.delay(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(request.path), str(request.user))
    return render(request, 'store/categories.html', {'categories': categories})

#кэширование всех категорий через представления
# @cache_page(60*2)
# def all_categories_cache(request):
#     return all_categories(request)



def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        games_searched = Games.objects.filter(name__icontains=searched)
        return render(request, 'store/search_games.html', {'searched': searched, 'games_searched':games_searched})
    else:
        return render(request, 'store/search_games.html', {})



class CommentUpdateView(UpdateView):
    template_name = 'comment/update.html'
    form_class = CommentForm
    queryset = Comment.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment/delete.html'
    success_url = reverse_lazy('store:index')