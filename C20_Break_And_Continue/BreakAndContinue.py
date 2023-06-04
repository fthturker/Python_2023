#break--> sadece ve sadece içindeki bulunduğu döngüyü sonlandırır
i = 0
while (i < 10):
    print("i: ",i)
    i +=1

i = 0
while (i < 10):
    if(i==5):
        break # i 5'e esit oldugunda donguyu durduracak
    print("i: ",i)
    i +=1

liste = [1,2,3,4,5,6,7,8,9]
for i in liste:
    if (i == 5):
        break
    print("i:",i)

# kullanıcı bize ismini soylesin bu ismi bastıralım.
# Ta ki kullanıcı "q" ya bastıgında dursun.
# while True:
#     isim=input("Adınızı Giriniz:")
#     print("Çıkmak için 'q' ya basın")
#     if(isim=="q"):
#         print("Programdan çıkılıyor...")
#         break
#     print("İsminiz:",isim)

#continue--> Döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle karşılaştığı zaman
             #geri kalan işlemlerini yapmadan direk bloğunun başına döner.

# liste = [1,2,3,4,5,6,7,8,9,10]
# for i in liste:
#     if(i==3 or i==5):
#         continue # 3 v3 5 degerlerini çıktıda göremiyouz
#     print("i:",i)

i = 0

while (i < 10):

    if (i == 2):
        i += 1 # Artırma işlemi
        continue

    print("i:",i)
    i += 1





