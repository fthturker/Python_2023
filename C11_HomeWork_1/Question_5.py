#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

a=input("a:")
b=input("b:")

print("Değiştirilmeden Önceki Değerler\na: {}\nb: {}".format(a,b))

a,b=b,a

print("Değiştirildikten Sonraki Değerler\na: {}\nb: {} ".format(a,b))