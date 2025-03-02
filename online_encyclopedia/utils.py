import os
from html import unescape

from django.conf import settings
from django.http import FileResponse, HttpResponse
import io

from django.template.defaultfilters import striptags
from django.utils.html import strip_tags
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter



from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# gsmp/static/gsmp/fonts/Noto_Sans_Georgian/NotoSansGeorgian-VariableFont_wdth,wght.ttf

def generate_pdf(post):
    pdfmetrics.registerFont(TTFont('NotoSansGeorgian', 'gsmp/static/gsmp/fonts/Noto_Sans_Georgian/NotoSansGeorgian-VariableFont_wdth,wght.ttf'))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{post.title}.pdf"'



    content = post.definition
    content1 = unescape(strip_tags(content))


    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = 'NotoSansGeorgian'
    styles['Normal'].encoding = 'UTF-8'
    story = []
    # სურათის დამატება
    # სრული ფაილური სისტემის ბილიკის გამოყენება

    try:
        if post.photo and post.photo.url:
            image_path = os.path.join(settings.MEDIA_ROOT, post.photo.name)
            story.append(Image(image_path, width=400, height=200))
    except:
        pass


    # ტექსტის გადატანა Paragraph-ის გამოყენებით

    # content = f"Title: {post.title}\nAuthor: {post.author}\nContent: {post.content}"
    contenti = f"<b>Title:</b> {post.title}<br/>  <b>Definition:</b> {content1}"
    story.append(Paragraph(contenti, styles['Normal']))

    doc.build(story)

    return response





#
# def generate_pdf(post):
#     # შექმენით HTTP პასუხი PDF ტიპისთვის
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="{post.title}.pdf"'
#
#     # buf = io.BytesIO()
#     # p = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     # # p.beginText()
#     # p.setTextOrigin(cm, cm)
#     # p.setFont("Helvetica", 30)
#
#
#
#     # PDF გენერაციისთვის canvas-ის ობიექტი
#     p = canvas.Canvas(response, pagesize=letter)
#     # TextObject შექმნა
#     text = p.beginText(100, 750)
#     text.setFont("Helvetica", 12)
#
#     content = f"Title: {post.title}\nAuthor: {post.author}\nContent: {post.content}"
#     for line in content.split('\n'):
#         text.textLine(line)
#
#     # TextObject-ის დახატვა
#     p.drawText(text)
#
#     # PDF-ის დახურვა და პასუხის დაბრუნება
#     p.showPage()
#     p.save()
#
#     return response
