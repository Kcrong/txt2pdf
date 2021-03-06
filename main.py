from reportlab.lib.colors import snow
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate

filename = 'images/test_png.png'

pdfmetrics.registerFont(TTFont('test', 'fonts/testfont.ttf'))

our_style = ParagraphStyle(name='custom_style',
                           fontName='test',
                           fontSize=30,
                           leading=10.1,
                           textColor=snow
                           )


def draw_background(canvas, document):
    canvas.drawImage('images/background.jpg', x=0, y=0,
                     # Default A1 size
                     width=594, height=841)


doc = SimpleDocTemplate("result.pdf")
parts = [
    Paragraph("Who am i?", our_style),
    Image(filename, width=400, height=400),
    Paragraph("I am 현우", our_style)

]

doc.build(parts, onFirstPage=draw_background)
