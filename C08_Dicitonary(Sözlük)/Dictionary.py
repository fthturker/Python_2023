# sozlugun icindeki her bir eleman indeks ile degil, anahtar(key) deger(value) olarak tutulur.
#sozluk olusturmak
# Süslü Parantez ve iki nokta (:) ile anahtar değerlerimizi yerleştirelim.
sozluk1 = {"sıfır":0,"bir":1,"iki":2,"üç":3}
print(sozluk1) # {'sıfır': 0, 'bir': 1, 'iki': 2, 'üç': 3}

print(type(sozluk1)) # <class 'dict'>

#Sözlük Değerlerine Erişmek ve Sözlüğe Değer Eklemek
#Öyleyse, bir değeri (value) elde etmek için, indeksleri değil anahtarları (key) kullanacağız.
print(sozluk1['iki']) # 2

# sozluge bes:5 degerini eklemek istiyoruz
sozluk1['bes']=5
print(sozluk1) # {'sıfır': 0, 'bir': 1, 'iki': 2, 'üç': 3, 'bes': 5}

#Temel Sözlük Metodları
yeni_sözlük = {"bir":1,"iki":2,"üç":3}
# values() metodu sözlüğün değerlerini(value) bir liste olarak döner.
print(yeni_sözlük.values()) # dict_values([1, 2, 3])

# keys() metodu sözlüğün anahtarlarını(key) bir liste olarak döner.
print(yeni_sözlük.keys()) # dict_keys(['bir', 'iki', 'üç'])

# items() metodu sözlüğün anahtar ve değerlerini bir liste içinde demet olarak döner.
print(yeni_sözlük.items()) # dict_items([('bir', 1), ('iki', 2), ('üç', 3)])

