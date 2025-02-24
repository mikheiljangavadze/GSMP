import os
from django.conf import settings
from django.http import FileResponse, HttpResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter



from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image


def generate_pdf(post):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{post.title}.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()
    story = []
    # სურათის დამატება
    # სრული ფაილური სისტემის ბილიკის გამოყენება
    if post.photo and post.photo.url:
        image_path = os.path.join(settings.MEDIA_ROOT, post.photo.name)
        story.append(Image(image_path, width=400, height=200))



    # ტექსტის გადატანა Paragraph-ის გამოყენებით

    # content = f"Title: {post.title}\nAuthor: {post.author}\nContent: {post.content}"
    content = f"<b>Title:</b> {post.title}<br/><b>Author:</b> {post.author}<br/><b>Content:</b> {post.content}"
    story.append(Paragraph(content, styles['Normal']))

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
