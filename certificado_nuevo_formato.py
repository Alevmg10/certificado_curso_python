from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
import qrcode
from codigoqr import generate_qr_code
from PIL import Image as PillowImage


class CertificateGenerator:
    def __init__(self, template_path, output_path="pdf_output/certificado_nuevo_formato.pdf"):
        self.template_path = template_path
        self.output_path = output_path
        self.c = None  # Canvas instance

    def resize_image(self, input_path, output_path, new_size):
        original_image = PillowImage.open(input_path)
        resized_image = original_image.resize(new_size)
        resized_image.save(output_path)


    def generate_certificate(self, nombre, cedula, codigo):
        # Create a PDF canvas
        self.c = canvas.Canvas(self.output_path, pagesize=landscape(letter))

        # Set the certificate template
        self.c.drawImage(self.template_path, 0, 0, width=landscape(letter)[0], height=landscape(letter)[1])

        # Agregar el nombre dinámicamente
        self.c.setFont("Helvetica", 64)
        # Calcular el centro de la página
        page_center_x = landscape(letter)[0] / 2
        # Calcular el ancho del texto
        text_width = self.c.stringWidth(nombre, "Helvetica", 64)
        # Calcular el punto de inicio para centrar el texto
        start_x = page_center_x - text_width / -28
        # Dibujar el texto centrado
        self.c.drawCentredString(start_x, 386, nombre)

        # Agregar numero de cedula dinámicamente
        self.c.setFont("Helvetica-Bold", 14)
        self.c.drawString(352, 366, cedula)

        # Agregar codigo QR
        qr = generate_qr_code("google.com")
        qr.save('templates/qr.png')
        qr_image_path = 'templates/qr.png'
        qr_image_resized = 'templates/temp/qr_resized.png'
        self.resize_image(qr_image_path, qr_image_resized, new_size=(100, 100))
        self.c.drawImage(qr_image_resized, 687, 512)

        # Agregar codigo
        self.c.setFont("Helvetica", 8)
        codigo_full = f"Codigo: {codigo}"
        self.c.drawString(80, 2, codigo_full)

        # Guardar el PDF
        self.c.save()

        print(f"Certificate generated: {self.output_path}")


# Ejemplo de uso
template_path = "templates/template_new.jpg"
generator = CertificateGenerator(template_path)
nombre_1 = "Anakin Skywalker"
nombre_2 = "Jon Doe"
nombre_3 = "Kerry Copito"
codigo_1 = "ebc1de695ec4682a9726281028afbed14ca263cd586ff709de252c61959111fa"
cedula_1 = "C.I. 20.420.202"
generator.generate_certificate(nombre_1, cedula_1, codigo_1)