from math import pi

# Lambda untuk menghitung luas lingkaran: L = pi * r^2
luas_lingkaran = lambda r: pi * r ** 2

# Contoh pemanggilan
print("Luas lingkaran (r = 7)  :", luas_lingkaran(7))
print("Luas lingkaran (r = 10) :", luas_lingkaran(10))

# Input dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))
print("Luas lingkaran:", round(luas_lingkaran(jari_jari), 2))
