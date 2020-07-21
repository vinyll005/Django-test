from django.db import models

# Create your models here.

class Article(models.Model):
    article_title = models.CharField('Article title', max_length= 200)
    article_text = models.TextField('Article text')
    pub_date = models.DateTimeField('Public date')

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Author naem', max_length=50)
    comment_text = models.CharField('Comment text', max_length=300)