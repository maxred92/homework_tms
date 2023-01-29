from django.db import models

# Create your models here.
class General_Store(models.Model):
    slug = models.SlugField()
    is_active = models.BooleanField(default=True, verbose_name='Is active?')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

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
    price = models.DecimalField(max_digits=5, verbose_name='Game Price', decimal_places=2)


    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
    
    def __str__(self):
        return f'{self.name}'



