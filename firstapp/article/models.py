# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    class Meta():
       db_table = 'artical'

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0) #blank=True, null=True

class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    commets_date = models.DateTimeField()
    comments_text = models.TextField(verbose_name='Текст комментария')
    comments_article = models.ForeignKey(Article)
    comments_from = models.ForeignKey(User)