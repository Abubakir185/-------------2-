hafta = int(input("Hafta kunini kiriting (1-7): "))

if hafta == 1:
    print("Dushanba") 
elif hafta == 2:
    print("Seshanba")
elif hafta == 3:
    print("chorshanba")
elif hafta == 4:
    print("Payshanba")
elif hafta == 5:
    print("Juma")
elif hafta == 6:
    print("Shanba")
elif hafta == 7:
    print("Yakshanba")
else:
    print("Bunday hafta kuni yo'q!")


oy = input("oy nomini kiriting: ").lower()

if oy == "yanvar" or oy == "fevral" or oy == "mart" or oy == "aprel" or oy == "may" or oy == "avgust" or oy == "sentyabr":
    print("Hozir o'qish vaqti!")
elif oy == "iyun" or oy == "iyul" or oy == "avgust":
    print("Ta'til.")
else : 
    print("Oy mavjud emas!")


rang = input("Svetafor rangini kiriting: ").lower()

if rang == "qizil":
    print("To'xtang!")
elif rang == "sariq":
    print("Tayyorlaning!")
elif rang == "yashil":
    print("Yurishingiz mumkin!")
else:
    print(f"Svetoforda {rang} rang yo'q!")


harf = input("1ta harf kiriting: ")

if harf .isupper():
    print(f'"{harf}" katta harf.')
else:
    print(f'"{harf}" kichik harf.')