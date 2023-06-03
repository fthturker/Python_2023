#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

if(a>=b and a>=c):
    print("En büyük sayı: ",a)
elif (b>=a and b>=c):
    print("En büyük sayı: ",b)
elif (c>=b and c>=a):
    print("En büyük sayı: ",c)