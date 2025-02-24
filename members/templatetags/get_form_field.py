from django import template
# from mp_news.models import Post, Tag


register = template.Library()

# @register.inclusion_tag('mp_news/popular_posts_tpl.html')
# def get_popular(cnt=4):
#     posts = Post.objects.order_by('-views')[:cnt]
#     return {"posts": posts}
#
# @register.inclusion_tag('mp_news/tags_tpl.html')
# def get_tags():
#     tags = Tag.objects.all()
#     return {"tags": tags}