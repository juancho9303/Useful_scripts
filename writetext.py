import PIL
from PIL import ImageFont, Image, ImageDraw

im = Image.open('A1033.jpg').convert('RGBA')

x, y =  im.size
eX, eY = 174, 174 #Size of Bounding Box for circle

bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
draw = ImageDraw.Draw(im)
draw.ellipse(bbox, outline = 'white')
del draw

txt = Image.new('RGBA', im.size, (255,255,255,0))

fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 30)

d = ImageDraw.Draw(txt)

d.text((800,10), "A", font=fnt, fill=(255,255,255,255))
d.text((800,60), "Scale", font=fnt, fill=(255,255,255,255))
d.text((800,110), "Kiloparsecs", font=fnt, fill=(255,255,255,255))
d.text((800,160), "z=", font=fnt, fill=(255,255,255,255))

im = Image.alpha_composite(im, txt)
im.save("marked.png")
im.show()
