from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils.html import strip_tags
from django.db.models import Q

from .utils import generate_pdf
from .models import OnlineEncyclopedia


def term_list(request):
    letter = request.GET.get('letter', None)  # იღებს ასოს GET პარამეტრიდან
    terms = OnlineEncyclopedia.objects.all().order_by('title')

    query = request.GET.get('q', '')  # იღებს ძებნის სიტყვას GET-დან
    search_type = request.GET.get('search_type', 'both')  # ადგენს ძებნის ტიპს
    page_number = request.GET.get('page', 1)  # გვერდის ნომერი

    if letter:
        terms = terms.filter(title__istartswith=letter)  # ფილტრავს ასოზე

    if query:
        if search_type == 'title':
            terms = terms.filter(title__icontains=query)  # მხოლოდ ტერმინის სახელში ეძებს
        elif search_type == 'definition':
            terms = terms.filter(definition__icontains=query)  # მხოლოდ დეფინიციაში ეძებს
        else:
            terms = terms.filter(Q(title__icontains=query) | Q(definition__icontains=query))  # ორივეში ეძებს

    paginator = Paginator(terms, 3)
    terms_page = paginator.get_page(page_number)


    context = {
        'terms': terms_page,
        'query': query,
        'search_type': search_type,

    }
    return render(request, 'online_encyclopedia/list.html',  context)

def term_detail(request, slug):
    term = get_object_or_404(OnlineEncyclopedia, slug=slug)
    return render(request, 'online_encyclopedia/detail.html', {'term': term})


def get_terms(request):
    terms = OnlineEncyclopedia.objects.all().values('title', 'slug')
    return JsonResponse({'terms': list(terms)})


def get_term_definition(request, slug):
    term = get_object_or_404(OnlineEncyclopedia, slug=slug)
    return JsonResponse({"definition": strip_tags(term.definition)[:400] + "..."})


def post_pdf_view(request, slug):
    post = get_object_or_404(OnlineEncyclopedia, slug=slug)


    return generate_pdf(post)