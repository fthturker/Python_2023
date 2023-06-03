#Liste olusturme
liste=[1,2,3,4,'Elma']
print(liste) # [1, 2, 3, 4, 'Elma']
print(type(list)) # <class 'type'>

liste=[]
print(liste) #[] bos liste

liste=[1,2,3,4,5,6,7,'elma','ayva']
print(len(liste)) # 9

liste=list("Merhaba")
print(liste) # ['M', 'e', 'r', 'h', 'a', 'b', 'a']
print(len(liste)) # 7

liste=[1,2,3,4,5,6,7,8,9,0]
print(liste[2]) # 3

print(liste[-1]) # 0

print(liste[2:6]) # [3, 4, 5, 6]

#bir listeyi birbirine toplama islemini stringlerdeki gibi yapabiliriz.
liste1=[1,2,3]
liste2=[4,5,6]
liste3=liste1+liste2
print(liste3) # [1, 2, 3, 4, 5, 6]

# list lerdeki veriler degistirilebilir
liste1=[1,2,3]
liste1[1]=10
print(liste1) # [1, 10, 3]

# append metodu --> verdiğimiz degeri listeye ekler
liste=[1, 2, 4]
liste.append("Murat")
print(liste) # [1, 2, 4, 'Murat']
# pop metodu
liste = [1,2,3,4,5]
liste.pop()

print(liste) # [1, 2, 3, 4]


# sort metodu
liste = [34,1,56,334,23,2,3,19]
liste.sort() # Küçükten büyüğe sıralar.
print(liste)

#İç içe Listeler
#Bir listenin içinde başka bir liste bulundurmak mümkündür.
# Bunlara Pythonda içiçe listeler denmektedir.
# Bu tip bir özellik, Pythonda ağaç yapılarında veya matris yapılarında oldukça kullanışlı olmaktadır.
# 3 Tane liste oluşturalım.
liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = [7,8,9]
yeniliste = [liste1,liste2,liste3]
print(yeniliste) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]