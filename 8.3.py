from PIL import Image, ImageDraw, ImageFont

n = input("Введите имя получателя: ")
im = Image.open('3.jpg')
f = ImageFont.truetype("beer-money12.ttf", 80)
draw = ImageDraw.Draw(im)
draw.text((120,105), n + ", от всего сердца, " , font = f, fill = "#a80000")
im.show()
im.save(n + 'otkr.png')


