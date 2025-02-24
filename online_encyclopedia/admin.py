import os

from django.contrib import admin
from .models import OnlineEncyclopedia
from django.db import models
from tinymce.widgets import TinyMCE
from django.contrib.admin.widgets import AdminTextareaWidget

# @admin.register(OnlineEncyclopedia)
# class OnlineEncyclopediaAdmin(admin.ModelAdmin):
#     class Media:
#         js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js',
#               'online_encyclopedia/js/tinymce_setup.js',
#               'online_encyclopedia/js/tinymce_autolink.js')


@admin.register(OnlineEncyclopedia)
class OnlineEncyclopediaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    class Media:
        js = (
              '/static/online_encyclopedia/js/tinymce_autolink.js')
# '/static/online_encyclopedia/js/tinymce_setup.js',
# admin.site.register(OnlineEncyclopedia, OnlineEncyclopediaAdmin)