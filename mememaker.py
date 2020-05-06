from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('base.jpg').convert('RGBA')

txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('fonts/Roboto-Bold.ttf', 15)
# get a drawing context
d = ImageDraw.Draw(txt)

# primo testo
d.text((90,90), """Creare il venv
all'interno
della cartella progetto""", font=fnt, fill=(0,0,0,255))
# secondo testo
d.text((270,55), """Creare il venv
fuori dalla
cartella progetto""", font=fnt, fill=(0,0,0,255))

out = Image.alpha_composite(base, txt)
out.show()

