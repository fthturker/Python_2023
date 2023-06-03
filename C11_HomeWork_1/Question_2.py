#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

boy=float(input("Boyunuz :"))
kilo=float(input("Kilonuz:"))

BKI=(kilo/boy**2)
print("Beden Kitle İndeksiniz Hesaplanıyor...")

print("boy: {}\nkilo: {}\nBKI : {} dir".format(kilo,boy,BKI))
