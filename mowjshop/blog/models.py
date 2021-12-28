from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


#1st Approach
#class PublishedManager(models.Manager):
 #   def published(self):
  #      return super(PublishedManager, self).get_queryset().filter(status='pulished')

#2nd approach


class PublishedManager(models.Manager):
    #overwrite
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='pulished')


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'چرک نویس'), ('published', 'منتشر شده'))
    # database colums
    title = models.CharField(max_length=250, primary_key=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish', allow_unicode=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    #model manager

#    objects = PublishedManager 1st approach


#2nd approach
    objects = models.Manager()
    published = PublishedManager()


class Meta:
    ordering = ('-poblish',)


def get_absolut_url(self):
    return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


def __str__(self):
    return self.title
