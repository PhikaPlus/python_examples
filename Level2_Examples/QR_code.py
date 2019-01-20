# Instagram: Phika.i
# "pypng" module must be installed for png format.
import pyqrcode

# data
qr_info = "Isn't fun???\nInstagram: Phika.ir"

# create QR
qr = pyqrcode.create(qr_info)

# create QR image (name + format)
qr.png('my_QRcode.png', scale = 10)
