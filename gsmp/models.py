from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Link')
    author = models.CharField(max_length=100, verbose_name='Author')
    content = HTMLField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo')
    views = models.IntegerField(default=0, verbose_name='Number of views')
    article_notes = models.TextField(blank=True, verbose_name=_('note'))
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gsmp:about', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Article(s)'
        verbose_name_plural = 'Articles'
        ordering = ['-created_at']



