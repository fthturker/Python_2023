print("""********************
Kullanıcı Girişi
********************
""")
sys_username = "fatih"
sys_password = "12345"

username = input("Kullanıcı Adı:")
password = input("Parola:")

if (username == sys_username and sys_password != password):
    print("Parola Hatalı...")
elif (username != sys_username and sys_password == password):
    print("Kullanıcı Adı hatalı...")
elif(username!=sys_username and sys_password!=password):
    print("Kullanıcı Adı ve Parola Hatalı...")
else:
    print("sisteme başarılı bir şekilde GİRİŞ yapıldı.")
