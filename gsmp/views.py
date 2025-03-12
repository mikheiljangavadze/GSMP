from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import path
from django.utils.translation import get_language, activate, gettext
from django.http import FileResponse
import io
from django.views.generic import DetailView, TemplateView
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter
from .models import Article
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

# @login_required
def index(request):
    context = {
        'title': _("GSMP - საქართველოს მოლეკულური პათოლოგიის საზოგადოება"),
    }
    return render(request, 'gsmp/index.html', context=context)



def about(request):
    return render(request, 'gsmp/about.html')

def newsall(request):
    return render(request, 'gsmp/newsall.html')

def mission(request):
    article = get_object_or_404(Article, slug="WhoWeAre")
    context = {
        'article': article,
    }
    return render(request, 'gsmp/mission.html', context=context)

def events(request):
    return render(request, 'gsmp/index.html',)

def resources(request):
    return render(request, 'gsmp/resources.html',)

def members(request):
    return render(request, 'gsmp/memberregistrationform.html',)


def director_board(request):
    article = get_object_or_404(Article, slug="who_we_are")
    context = {
        'article': article,
    }
    return render(request, 'gsmp/director_board.html', context=context)

def advisory_board (request):
    article = get_object_or_404(Article, slug="WhoWeAre")
    context = {
        'article': article,
    }
    return render(request, 'gsmp/advisory_board.html', context=context)

def who_we_are(request):
    article = get_object_or_404(Article, slug="who_we_are")
    context = {
        'article': article,
    }
    return render(request, 'gsmp/who_we_are.html', context=context)

def history(request):
    article = get_object_or_404(Article, slug="who_we_are")
    context = {
        'article': article,
    }
    return render(request, 'gsmp/history.html', context=context)

