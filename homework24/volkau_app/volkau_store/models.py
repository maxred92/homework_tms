from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import Avg
from django.urls import reverse

# Create your models here.
class General_Store(models.Model):
    slug = models.SlugField()
    is_active = models.BooleanField(default=True, verbose_name='Is active?')
    description = RichTextField(null=True, blank=True, verbose_name='Description')

    class Meta:
        abstract = True
        



class Category(General_Store):
    title = models.CharField(max_length=100, verbose_name='Category Title')  
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated at')
    games_number = models.IntegerField(default=0, verbose_name='Games number')
    

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return f'{self.title}'


class Games(General_Store):
    name = models.CharField(max_length=100, verbose_name='Game Name')
    game_image = models.ImageField(upload_to='game', null=True, blank=True, verbose_name='Game Image')
    category = models.ForeignKey(Category, verbose_name='Game Category', on_delete=models.SET_NULL, null=True, blank=True)
    release_date = models.DateField(verbose_name='Game Release')
    public_date = models.DateField(auto_now_add=True, verbose_name='Game Public')
    price = models.PositiveSmallIntegerField(verbose_name='Game Price')


    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        indexes = [models.Index(fields=['name'], name='games_names_idx')]
        ordering=('name',)
    
    def get_rating(self):
        result = Comment.objects.filter(game=self).aggregate(Avg('rating'))
        return f"{result['rating__avg']}"
    
    def __str__(self):
        return f'{self.name}'



class Comment(models.Model):  
    game = models.ForeignKey(Games,  
			     on_delete=models.CASCADE,  
			     related_name='comments')  
    name = models.CharField(max_length=80)  
    email = models.EmailField()  
    body = models.TextField()  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    active = models.BooleanField(default=True)
    rating = models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Rating game')  
      
    class Meta:  
        ordering = ('created',)  
          
    def __str__(self):  
        return f'{self.name} {self.body}'
    
    def get_absolute_url(self):
        return reverse('store:game_slug', kwargs={'game_slug': self.game.slug})