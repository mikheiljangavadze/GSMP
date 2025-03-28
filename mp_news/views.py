from typing import Any, Dict
from django.db.models.query import QuerySet
from .utils import generate_pdf
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag, Comment
from django.db.models import F
from django.core.paginator import Paginator
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def post_pdf_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return generate_pdf(post)





class NewsHome(ListView):
    model = Post
    template_name = 'mp_news/index.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        pinned_post = Post.objects.latest('created_at')
        pinned_post.views = F('views') + 1
        pinned_post.save()
        pinned_post.refresh_from_db()
        context['pinned_post'] = pinned_post
        context['title'] = 'სიახლეები'

        categories = Category.objects.all()
        latest_posts_by_category = {}
        for category in categories:
            latest_posts_by_category[category.slug] = Post.objects.filter(category=category)[:2]

        context['latest_posts_by_category'] = latest_posts_by_category
        return context


class PostsByCategory(ListView):
    template_name = 'mp_news/category.html'
    context_object_name = 'posts'
    paginate_by = 8
    # allow_empty = False
    msg = ''
    def get_queryset(self):
        queryset = Post.objects.filter(category__slug=self.kwargs['slug']).order_by('-created_at')
        if not queryset.exists():
            self.msg = " - სტატიები ამ კატეგორიაში არ მოიძებნა"
            pass

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(Category.objects.get(slug=self.kwargs['slug'])) + str(self.msg)
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'mp_news/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()

        comments = Comment.objects.filter(post=self.object, is_published=True).order_by('-created_at')
        paginator = Paginator(comments, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['comments'] = page_obj

        return context


class PostsByTag(ListView):
    template_name = 'mp_news/tag.html'
    context_object_name = 'posts'
    paginate_by = 8
    # allow_empty = False
    msg1 = ' '
    def get_queryset(self, **kwargs):
        queryset = Post.objects.filter(tags__slug=self.kwargs['slug']).order_by('-created_at')
        if not queryset.exists():
            self.msg1 = "  არ მოიძებნა"
            pass
        return queryset

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'სტატია ტეგზე: ' + str(Tag.objects.get(slug=self.kwargs['slug'])) + str(self.msg1)
        return context





class Search(ListView):
    template_name = 'mp_news/search.html'
    context_object_name = 'posts'
    paginate_by = 8


    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}"
        context['title'] = "ძიების შედეგი"
        return context


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post, is_published=True).order_by('-created_at')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        comment_text = request.POST.get('comment')

        name_valid = len(username) >= 2 and all(c.isalnum() or c.isspace() or c in '- ' for c in username)

        try:
            validate_email(email)
            email_valid = True
        except ValidationError:
            email_valid = False

        comment_valid = len(comment_text) >= 2 and all(c.isalnum() or c in ',.-_!? ' for c in comment_text)

        if not (name_valid and email_valid and comment_valid):
            errors = {
                'username': 'Invalid input' if not name_valid else '',
                'email': 'Invalid input' if not email_valid else '',
                'comment': 'Invalid input' if not comment_valid else '',
            }

            context = {
                'post': post,
                'comments': comments,
                'errors': errors,
            }
            return render(request, 'mp_news/single.html', context)

        post = Post.objects.get(pk=post_id)
        comment = Comment(username=username, email=email, comment=comment_text, post=post)
        comment.save()

        response_data = {
            'success': True,
            'username': comment.username,
            'created_at': comment.created_at.strftime('%d %B %Y'),
            'comment': comment.comment,
        }
        return JsonResponse(response_data)

    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, 'mp_news/single.html', context)