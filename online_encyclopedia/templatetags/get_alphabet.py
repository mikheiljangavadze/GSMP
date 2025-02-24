import re
from django import template
from django.urls import reverse
from django import template
import gsmp.views as views
from mp_news.models import Post
from django.utils.translation import gettext_lazy as _





register = template.Library()



@register.simple_tag()
def get_alphabet(lang):

    if lang == "ka":
        alphabet = [chr(x) for x in range(0x10D0, 0x10F0)]  # ქართული ანბანი

    else:
        alphabet = [chr(x) for x in range(65, 91)]  # ინგლისური ანბანი (A-Z)
        #
        # alphabet_ka = [chr(x) for x in range(0x10D0, 0x10F0)]  # ქართული ანბანი
        # alphabet_en = [chr(x) for x in range(65, 91)]  # ინგლისური ანბანი (A-Z)
    return alphabet