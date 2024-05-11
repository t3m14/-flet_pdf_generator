from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import fitz  # PyMuPDF



import qrcode
def create_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

def get_image_of_pdf(pdf_file):
    # Открываем PDF файл
    pdf_document = fitz.open("out.pdf")
    page = pdf_document[0]
    image = page.get_pixmap()
    image.save("out.png")
    pdf_document.close()
def draw_pdf(name, price):
    # name = name.decode('utf-8')
    try:
        c = canvas.Canvas("out.pdf", pagesize=(100, 100))
        c.rect(10, 10, 80, 80, fill=0, stroke=1)
        pdfmetrics.registerFont(TTFont('oswald', 'oswald.ttf'))
        c.setFont("oswald", 12)
        c.drawString(20, 70, name)
        c.setFont("Times-Roman", 12)
        c.drawString(30, 50, f"{price} P.")
        create_qr_code(f"{name} - {price} P.", 'qrcode.png')
        c.drawInlineImage('qrcode.png', 35, 20, width=20, height=20)
        c.showPage()
        c.save()
    except Exception as e:
        print(e)
