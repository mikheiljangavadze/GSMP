from django import template
from mp_news.models import Post, Tag


register = template.Library()

@register.inclusion_tag('mp_news/popular_posts_tpl.html')
def get_popular(cnt=4):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}

@register.inclusion_tag('mp_news/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}


# @register.filter
# def highlight_terms(text):
#     terms = OnlineEncyclopedia.objects.all()
#     for term in terms:
#         term_pattern = re.compile(rf'\b({re.escape(term.title)})\b', re.IGNORECASE)
#         term_link = f'<a class="encyclopedia-term" href="{reverse("online_encyclopedia:online_encyclopedia_details", kwargs={"slug": term.slug})}" data-slug="{term.slug}">{term.title}</a>'
#         text = term_pattern.sub(term_link, text)
#     return text