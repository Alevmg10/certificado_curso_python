import qrcode

def generate_qr_code(string):
  """
  Genera un código QR a partir de una cadena de texto.

  Args:
    string: La cadena de texto que se utilizará para generar el código QR.

  Returns:
    Una imagen con el código QR.
  """

  # Importar la biblioteca qrcode
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4
  )

  # Agregar la cadena de texto al código QR
  qr.add_data(string)
  # Generar la imagen del código QR
  qr_image = qr.make_image()
  # Devolver la imagen del código QR
  return qr_image


# Ejemplo de uso

string = "https://www.ssn.com.ve/"
qr_image = generate_qr_code(string)
qr_image.save("qr.png")

# Mostrar la imagen del código 
