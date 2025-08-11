from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'Автор: {self.user.username}'
    
    def update_rating(self):
        post_rating = sum(post.rating for post in self.post_set.all()) * 3
        comment_rating = sum(comment.rating for comment in self.user.comment_set.all())
        post_comment_rating = sum(comment.rating for comment in Comment.objects.filter(post__author=self))

        
        self.rating = post_rating + comment_rating + post_comment_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):

    ARTICLE = 'AR'
    NEWS = 'NW'

    POST_TYPES = [
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость')
    ]

    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POST_TYPES, default=ARTICLE)
    time_create = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} ({self.get_post_type_display()})'
    
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
    
    def preview(self):
        return self.text[:124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} — {self.сategory.name}'
    
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'Комментарий от {self.user.username} к "{self.post.title}"'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
