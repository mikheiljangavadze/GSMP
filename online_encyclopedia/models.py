from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify


class OnlineEncyclopedia(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    definition = HTMLField()  # განმარტება

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title