import qrcode
import os
from PIL import Image, ImageDraw

# Stickers ka folder banana
if not os.path.exists('DataX_Stickers'):
    os.makedirs('DataX_Stickers')

base_url = "https://data-x598.github.io/data-x/"

print("Stickers ban rahe hain, thora intezar karein...")

for i in range(1, 501):
    serial = f"{i:04d}"
    url = base_url + serial
    
    # QR Code banana
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Niche Serial Number likhne ke liye jagah banana
    w, h = img.size
    canvas = Image.new('RGB', (w, h + 50), 'white')
    canvas.paste(img, (0, 0))
    draw = ImageDraw.Draw(canvas)
    
    # Serial Number likhna (SN: 0001 format mein)
    draw.text((w//2 - 35, h + 10), f"SN: {serial}", fill="black")
    
    # Save karna
    canvas.save(f"DataX_Stickers/QR_{serial}.png")

print("Zabardast! 500 Stickers 'DataX_Stickers' folder mein tayyar hain.")
