from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


ARTICLE_TYPE = (('P', 'PUBLISHED'),('D', 'DRAFT'),)


class Article(models.Model):
    heading = models.CharField(max_length=64)
    discription = models.CharField(max_length=256)
    dp = models.CharField(max_length=256)
    a_type = models.CharField(max_length=1, choices=ARTICLE_TYPE)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    creation_date = models.DateField(auto_now=True)
    slug = AutoSlugField(populate_from='heading', unique=True)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        ordering = ["-creation_date"]

    def __str__(self):
        return str(self.heading)


class Photos(models.Model):
    discription = models.CharField(max_length=256)
    image = models.ImageField(upload_to='./imagestore')
    date = models.CharField(max_length=8)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
        ordering = ["-date"]

    def __str__(self):
        return str(self.date) + ' - ' + str(self.discription)[0:30]


