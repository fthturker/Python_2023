# print() fonksiyonu
print("Fatih")  #Fatih
print(44)   #44

a=15
b=13
print(a+b)  #28


"""
Stringlerdeki özel karakterler
\n --> print() fonksiyonu stringlerde boyle bir karakterle karsilasirsa 
       alt satirdan ekrana yazdirma islemine devam eder.
\t --> print() fonksiyonu stringlerde boyle bir karakterle karsilasirsa 
       bir tab bosluk birakarak ekrana yazdirma islemine devam eder.       
"""
print("Python\nProgramlama\nDilidir")
print("Python\tProgramlama\tDilidir")

# type() --> icine gonderilen degerin hangi veri tipinden oldugunu soyler
#Integer (Tamsayi) turu
a=34
print(type(a))  # <class 'int'>
# Float (Ondalikli sayi) turu
b=3.14
print(type(b))  # <class 'float'>
# String (Karakter Dizisi) turu
c="Fatih"
print(type(c))  #  <class 'str'>

"""
print() fonk. ozellikleri
sep parametresi --> yazdirdigimiz degerlerin arasina istedigimiz karakterlerin yerlestirilmesini saglar.
                    Eger bu parametreyi kullanmazsak degerlerin arasina varsayilan olarak bosluk yerlestirilir.
"""
print(3,4,5,6,7,8)  # 3 4 5 6 7 8
# sep parametresi sayesinde degerlerin arasina nokta konuyor
print(3,4,5,6,7,8,sep=".")  # 3.4.5.6.7.8
# degerlerin arasinda "/" sembolu yerlestiriliyor
print("Ali","Veli","Fatih",sep="/") # Ali/Veli/Fatih

"""
Yildizli parametreler
eger bir string'in basina * isareti koyup print fonksiyonuna gonderirsek bu string karakterlerine
ayrılacak ve her bir karakter ayri birer string olarak davranilarak ekrana basilacaktir.
"""
#varsayilan olarak karakterlerin arasina bosluk konuluyor
print("python")     #python
print(*"python")    #p y t h o n

"""
formatlama--> programlama yaparken bazi yerlerde bir stringin icinde daha onceden tanimli 
              string,float,int vs. degerleri yerlestirmek isteyebiliriz. Boyle durumlar icin python'da 
              format() fonk. bulunmaktadir.  
"""
# Burada 3 tane süslü parantezimiz ({}) var ve bunların yerine sırasıyla format fonksiyonun içindeki değerler geçiyor.
print("{} {} {}".format(3.1423,5.324,7.324324)) # 3.1423 5.324 7.324324
a = 3
b = 4

print("{} + {} 'nin toplamı {} 'dır".format(a,b,a+b)) # 3 + 4 'nin toplamı 7 'dır

# Süslü parantezlerin içindeki sayılar format fonksiyonun içinden hangi sıradaki değerin geleceğini söylüyor.
print("{1} {0} {2}".format(43,"Murat",54)) # Murat 43 54

# Süslü parantezlerin içindeki kullanım ondalıklı kısmın sadece 2 basamağına kadar almak istediğimiz söylüyor.
print("{:.2f} {:.2f} {:.3f}".format(3.1463,5.324,7.324324)) # 3.15 5.32 7.324




