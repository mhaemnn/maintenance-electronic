# Belajar latihan logika dan komparasi

user = float(
    input("Masukan angka yang bernilai \n dari 3 \n atau \n lebih dari 10 \n"))

# Memeriksa angka kurang dari 3
# ++++3-------------
kurang = (user < 3)
print("kurang dari 3: ", kurang)

# Memeriksa angka lebih dari 10
# --------10++++++
lebih = (user < 10)
print("lebih dari 10: ", lebih)


# Menggabungkan
hasil = kurang or lebih
print("angka yang anda masukan: ", hasil)
