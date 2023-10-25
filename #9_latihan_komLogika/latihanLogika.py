# Belajar Latihan logika dan komparasi
user = float(input(
    "MASUKAN ANGKA YANG BERNILAI \n kurang dari 3 \n atua \n lebih dari 10 \n :"))

kurang = (user < 3)
print("kurang dari 3: ", kurang)

lebihDari = (user > 10)
print("lebih darii 10:", lebihDari)

iscorect = kurang or lebihDari
print("angka yang ada masukan: ", iscorect)
