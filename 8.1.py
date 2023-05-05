from PIL import Image
im = Image.open('1.jpg')
im.crop((50,100,950,410)).save('2.jpg')


