from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):

    id = models.IntegerField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    login = models.TextField(validators=[
                            RegexValidator(r'^[A-Za-z][A-Za-z0-9_]{6,10}$',
                            message = 'Bad login',
                            code = 'Invalid login')
                            ])
    email = models.TextField(validators=[
                            RegexValidator(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[by]$',
                            message='Incorrect mail',
                            code='Invalid email')
                            ])
    register = models.TextField()
    def __str__(self):
        return f"Name: {self.first_name} Last name: {self.last_name}"

class Category(models.Model):

    category_id = models.IntegerField(primary_key=True)
    category_title = models.TextField()
    def __str__(self):
        return f"Category: {self.category_title}"

class Post(models.Model):

    title = models.TextField()
    data_created = models.TextField()
    content = models.TextField()
    post_author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_category_id = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"Title: {self.title}/{self.post_category_id} - Date of creation: {self.data_created}"