
import pyqrcode
import png
from pyqrcode import QRCode
  
s = "www.codingforfree.com"
  
url = pyqrcode.create(s)
  
url.svg("qr.svg", scale = 8)
  
url.png('qr.png', scale = 8)
