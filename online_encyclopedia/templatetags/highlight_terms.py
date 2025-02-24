import re
from django import template
from django.urls import reverse
from online_encyclopedia.models import OnlineEncyclopedia  # შეცვალე შენი აპის სახელით

register = template.Library()

@register.filter
def highlight_terms(text):
    terms = OnlineEncyclopedia.objects.all()
    for term in terms:
        term_pattern = re.compile(rf'\b({re.escape(term.title)})\b', re.IGNORECASE)
        term_link = f'<a class="encyclopedia-term" href="{reverse("online_encyclopedia:online_encyclopedia_details", kwargs={"slug": term.slug})}" data-slug="{term.slug}">{term.title}</a>'
        text = term_pattern.sub(term_link, text)
    return text