# String olusturma
# bir string'den bir degisken olusturabiliriz
a = 'Fatih'
b = "Turker"
c = """Yavuz"""
print(a)  # Fatih
print(b)  # Turker
print(c)  # Yavuz

# String indeksleme parcalama
a = "Pythonu cok seviyorum"
# 0. elemana ulasalım. bunun icin [] operatorunu kullanacagiz
print(a[0])  # P
# sondaki eleman -1 yazilir
print(a[-1])  # m

# String parcalama söyle--> [baslama indeksi : bitis indeksi : atlama degeri]
a = "Pythonu cok seviyorum"
print(a[2:9:2])  # touc

# stringi tersten cevirir
print(a[::-1])  # muroyives koc unohtyP

# STRING OZELLIKLERI
# bir string'in uzunlugunu bulma --> len()
a = "Pythonu cok seviyorum"
print(len(a))  # 21
# bir string'in karakterlerini direk degistiremiyoruz.
# Cunku string'ler boyle bir islemi desteklemiyor.

# Python'da stringleri toplayalim yani birbirine ekleyelim.
a = 'Python'
b = 'Programlama'
c = 'Dili'
print(a+' '+ b+' '+c)  #Python Programlama Dili

print(a*3) # PythonPythonPython
