from PIL import Image, ImageDraw, ImageFilter

im = Image.open('./fullmoon.png')

mask_im = Image.new("L", im.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((0,0,100,100), fill=255)
mask_im.save('./mask_circle.png')

