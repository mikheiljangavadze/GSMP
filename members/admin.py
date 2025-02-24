from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from members.models import GsmpMember

admin.site.register(GsmpMember, UserAdmin)