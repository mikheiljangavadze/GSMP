from django import template
import gsmp.views as views
from mp_news.models import Post
from django.utils.translation import gettext_lazy as _





register = template.Library()


@register.inclusion_tag('gsmp/tags/news.html')
def get_last_news():
    news = Post.objects.order_by("-id")[:7]
    last_news = news[0]
    last_news_group = news[1:7]
    return {"last_news": last_news,  "last_news_group": last_news_group}


@register.simple_tag()
def get_main_menu():
    main_menu = [{'title': 'GSMP', 'url_name': 'gsmp:home'},
                 {'title': _('ჩვენს შესახებ'), 'url_name': 'gsmp:about',  'submenu': [
                     {'title': _('ასოციაციის შესახებ'), 'url_name': 'gsmp:who_we_are', 'submenu': [
                         {'title': _('ვინ ვართ ჩვენ'), 'url_name': 'gsmp:who_we_are'},
                         {'title': _('ჩვენი მიზნები'), 'url_name': 'gsmp:mission'},
                         {'title': _('ისტორია'), 'url_name': 'gsmp:history'},
                         {'title': _('დირექტორთა საბჭო'), 'url_name': 'gsmp:director_board'},
                         {'title': _('მრჩეველთა საბჭო'), 'url_name': 'gsmp:advisory_board'},

                     ]},
                     {'title': _('კომიტეტები'), 'url_name': 'gsmp:about', 'submenu': [
                         {'title': _('საგარეო'), 'url_name': 'gsmp:about'},
                         {'title': _('მეცნიერების'), 'url_name': 'gsmp:about'},
                     ]},
                     {'title': _('სამუშაო ჯგუფები'), 'url_name': 'gsmp:resources', 'submenu':[
                         {'title': _('ონკოჰემატოლოგია'), 'url_name': 'gsmp:about'},
                         {'title': _('ფარმაკოგენეტიკა'), 'url_name': 'gsmp:about'},
                     ]},
                     {'title': _('GSMP სიახლები'), 'url_name': 'mp_news:newshome', 'submenu': [
                         {'title': _('GSMP სიახლები'), 'url_name': 'gsmp:about'},
                         {'title': _('GSMP წლიური ანგარიში'), 'url_name': 'gsmp:about'},
                     ]},
                 ]},



                 {'title': _('სიახლეები'), 'url_name': 'mp_news:newshome'},
                 {'title': _('ღონისძიებები'), 'url_name': 'gsmp:events'},
                 {'title': _('რესურსები'), 'url_name': 'gsmp:resources', "submenu":  [
                         {'title': _('Online Encyclopedia'), 'url_name': 'online_encyclopedia:online_encyclopedia_home'},
                         {'title': _('გაიდლაინები'), 'url_name': 'gsmp:about'},

                 ]},

                 {'title': _('წევრობა'), 'url_name': 'members:register'}
                 ]

    return main_menu

@register.simple_tag()
def get_side_bar_menu(requested_url):
    main_menu = get_main_menu()
    x=0
    i=[]
    while i != requested_url:
        item = main_menu[x]
        i = item['url_name']
        x += 1

    menu_sidebar = item
    return  menu_sidebar




    # main_menu = [{'title': 'GSMP', 'url_name': 'gsmp:home'},
    #             {'title': _('ჩვენს შესახებ'), 'url_name': 'gsmp:about',  "submenu": [
    #                 {"title": "Nature", "url_name": "members:register"},
    #                 {"title": "Medical", "url_name": "gsmp:resurses"},
    #                 {"title": "Science", "url_name": "gsmp:events", "submenu": [
    #                     {'title': _('სიახლეები'), 'url_name': 'mp_news:newshome'},
    #                     {'title': _('სედე'), 'url_name': 'gsmp:resurses'},
    #                  ]},
    #                 ]},
    #
    #
    #
    #             {'title': _('სიახლეები'), 'url_name': 'mp_news:newshome'},
    #             {'title': _('ღონისძიებები'), 'url_name': 'gsmp:events'},
    #             {'title': _('რესურსები'), 'url_name': 'gsmp:resurses'},
    #             {'title': _('წევრობა'), 'url_name': 'members:register'},
    #             ]



# @register.simple_tag
# def get_news(news_var):
#     last_news = Post.objects.order_by("id")[:7]
#     news_item = last_news[news_var]
#
#     return news_item

#
# @register.simple_tag
# def get_menu():
#     return menu

# @register.simple_tag()
# def get_diag_dragt_list():
# 	return Diag_Draft.objects.all()
#
#
# @register.inclusion_tag('DJtest/draft_list.html')
# def show_drafts():
# 	drafts = Diag_Draft.objects.all()
# 	return {"drafts": drafts}
#
#
# @register.simple_tag()
# def to_str(value):
# 	return str(value)
#
#
