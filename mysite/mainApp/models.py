from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    titel = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.titel)

class Tag(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.titel)