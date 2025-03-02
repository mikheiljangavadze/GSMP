from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter
from .models import Article

from django.template.loader import render_to_string

from django.http import HttpResponse
from django.shortcuts import get_object_or_404


from gsmp.models import Article  # შეცვალე შენი მოდელის სახელით


# @login_required
def index(request):
    # activate('ka')
    # context = {}
    # trans =  translate(language='ka'){'trans': trans}
    return render(request, 'gsmp/index.html',)


# def translate(language):
#     cur_language = get_language()
#     try:
#         activate(language)
#         text = gettext('გამარჯობა')
#     finally:
#         activate(cur_language)
#     return text


def about(request):

    return render(request, 'gsmp/about.html')


def mission(request):
    article = get_object_or_404(Article, slug="WhoWeAre")

    context = {
        'article': article,
    }

    return render(request, 'gsmp/mission.html', context=context)




def news(request):

    return render(request, 'gsmp/index.html',
                )


def events(request):

    return render(request, 'gsmp/index.html',
                  )


def resources(request):

    return render(request, 'gsmp/resources.html',
                   )


def members(request):

    return render(request, 'gsmp/memberregistrationform.html',
                   )




def director_board(request):
    article = get_object_or_404(Article, slug="WhoWeAre")

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









