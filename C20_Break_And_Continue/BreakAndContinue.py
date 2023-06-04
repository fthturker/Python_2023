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
while True:
    isim=input("İsim: (Çıkmak için 'q' ya basın):" )
