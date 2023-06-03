#python'da kullanıcıdan girdi almamızı saglayan input() fonksiyonu bulunmaktadır.

# input() fonksiyonu
#print(input('lütfen bir sayi giriniz...\n'))

#a=input("lütfen bir sayi giriniz...\n")
#print("kullanicinin girdiği sayi: ",a)  # kullanicinin girdiği sayi:  45

# kullanicinin girdiği input fonksiyonundan bize string olarak döner
#a=input("lütfen bir sayi giriniz...\n")
#print(type(a)) # <class 'str'>

# Eğer biz bir sayi ile işlem yapacaksak kullanıcıdan aldığımız değere (string)
# float ya da int fonksiyonuyla veri tipi dönüstürme işlemi yapmamız gherekir

#a=int(input("lütfen bir sayi giriniz...\n"))
#print(a*3)

# üç tane sayiyi alıp toplamlarını ekrana yazdiralim
a = int(input("Birinci Sayı:")) #10
b = int(input("İkinci Sayı:"))  #20
c = int(input("Üçüncü Sayı:"))  #30

print("Toplamları:", a+b+c) #60

