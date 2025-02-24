from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

from tinymce.widgets import TinyMCE
from django.db import models

from django.contrib.auth.admin import UserAdmin

admin.site.register(Article)