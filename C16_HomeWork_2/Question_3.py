"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""
vize1 = int(input("Vize1:"))
vize2 = int(input("Vize2:"))
final = int(input("Final:"))


genel_not =  vize1 * 3/10 + vize2 * 3/10 + final * 4/10
print("Notunuz:",genel_not)

if (genel_not>=90):
    print("Harf Notunuz AA")
elif (genel_not>=85):
    print("Harf Notunuz AB")
elif (genel_not>=80):
    print("Harf Notunuz BA")
elif (genel_not>=75):
    print("Harf Notunuz BB")
elif (genel_not>=70):
    print("Harf Notunuz CB")
elif (genel_not>=65):
    print("Harf Notunuz CC")
elif (genel_not>=60):
    print("Harf Notunuz DD")
elif (genel_not>=55):
    print("Harf Notunuz FD")
else:
    print("Harf Notunuz FF")

