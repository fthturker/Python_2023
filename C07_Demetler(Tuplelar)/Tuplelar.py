demet=(1,2,3,4,5)
print(type(demet)) # <class 'tuple'>

print(demet[4]) # 5

# demetlerin metodları
# index --> icine verdigimiz elemanin hangi indekste oldugunu bulabiliriz
demet = (1,2,3,"Mustafa","Murat","Coşkun")
# "Mustafa" elemanının indeksini buluyoruz.
print(demet.index('Mustafa')) # 3

#count ---> kaç tane gectigini
demet=(1,2,2,3,4,5,6,1,1,2,3,1,1)
print(demet.count(1)) # 5