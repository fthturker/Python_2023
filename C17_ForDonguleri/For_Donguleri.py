# in Operatörü
# bir elemanın başka bir listede,demette veya stringte
# (karakter dizileri) bulunup bulunmadığını kontrol eder.

print(5 in [1, 2, 3, 4, 5])  # True

print("p" in "python")  # True

print(4 in {1, 2, 3, 4})  # True

print(not 3 in {1, 2, 4, 5})  # True

"""
for Döngüsü , listelerin ,demetlerin, stringlerin ve hatta sözlüklerin üzerinde dolaşmamızı sağlayan
 bir döngü türüdür. Yapısı şu şekildedir.

        for eleman in veri_yapısı(liste,demet vs):
            Yapılacak İşlemler
Bu yapı bize şunu söyler;

        eleman değişkeni her döngünün başında listenin,demetin vs. her bir elemanına eşit olacak 
        ve her döngüde bu elemanla işlem yapılacak.
"""
liste = [1, 2, 3, 4, 5, 6, 7]
for i in liste:
    print(i)

toplam = 0
liste = [1, 2, 3, 4, 5, 6, 7]
for i in liste:
    toplam = toplam + i
    print("Toplam: {} Eleman: {}".format(toplam, i))
print(toplam)

liste = [1, 2, 6, 8, 12, 13, 17, 20, 46]
for i in liste:
    if i % 2 == 0:
       print(i)

s="python"
for i in s:
    print(i)
    print(i*3)

liste = [(1,2),(3,4),(5,6),(7,8)]
for i in liste:
    print(i)

for (i,j) in liste:
    print("i: {} j: {}".format(i,j))

liste = [(1,2,3),(3,4,5),(5,6,7),(7,8,9)]
for (i,j,k) in liste:
    print("i: {} j: {} k: {}".format(i,j,k))

sozluk = {"bir":1,"iki":2,"üç":3,"dört":4}
for i in sozluk.keys():
    print(i)

for i in sozluk.values():
    print(i)

for i in sozluk.items():
    print(i)