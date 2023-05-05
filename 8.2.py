from PIL import Image
c = {1:'dr.jpg',2:'god.jpg',3:'medic.jpg',4:'russia.jpg',5:'svarschika.jpg'}

print(" С Днём рождения -- 1\n","С Новым годом -- 2\n","С днём медика -- 3\n","С днём России -- 4\n","С Днём Сварщика -- 5")
a = int(input("Для получения открытки введите число - номер прадника : "))
im = Image.open(c[a])
im.show()
