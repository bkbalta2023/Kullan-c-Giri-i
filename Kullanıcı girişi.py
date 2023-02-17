print("""
****************
Kullanici Girisi
****************
""")

s_kullanici = "bkbalta2023"
s_parola = "1995Balta"

kullanici = input("Kullanici Adi: ")
parola = input("Parola: ")

if (s_kullanici == kullanici and parola == s_parola):
    print("Basari ile giris yaptiniz.")
elif (s_kullanici == kullanici and s_parola != parola):
    print("Parola Yanlis!")
elif (s_kullanici != kullanici and s_parola == parola):
    print("Kullanici adi yanlis!")
elif (s_kullanici != kullanici and s_parola != parola):
    print("Kullanici adi ve parola yanlis")