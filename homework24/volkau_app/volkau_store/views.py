from django.shortcuts import get_object_or_404, render
from volkau_store.models import Games, Category, Comment
from .forms import CommentForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpRequest
from django.core.paginator import Paginator
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

# Create your views here.




def game(request, game_slug):
    game = get_object_or_404(Games, slug=game_slug)
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
    return render(request,  
		  'store/game.html',  
		  {'game': game,  
		  'comments': comments,  
		  'new_comment': new_comment,  
		  'comment_form': comment_form,
          'average_rating': average_rating})

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
    context = {
        'category' : category,
        'games_category' : games_category
    }
    return render(request, 'store/category.html', context)


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})



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