# islem = input("İşlem giriniz:")
#
# if islem == "1":
#     print("islem 1 secildi.")
# elif islem == "2":
#     print("islem 2 secildi.")
# elif islem == "3":
#     print("islem 3 secildi.")
# elif islem == "4":
#     print("islem 4 secildi.")
# elif islem <= "0":
#     print("Sıfır veya Negatif sayi girmeyiniz")
# elif islem > "4":
#     print("4'den büyük sayi girmeyiniz!!!")
# else:
#     print("Gecersiz işlem!")

note = float(input("Notunuzu giriniz:"))

if (note >= 90):
    print("AA")
elif (note >= 85):
    print("BA")
elif (note >= 80):
    print("BB")
elif (note >= 75):
    print("CB")
elif (note >= 70):
    print("CC")
elif (note >= 65):
    print("DC")
elif (note >= 60):
    print("DD")
else:
    print("Kaldınız!!!")
