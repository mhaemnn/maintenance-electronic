# Belajar string

print('\n', 40*"=", '\n')
# Penulisan string
"""
1. menggunakan single qoute
2. menggunakan double qoute
3. menggunakan \
4. backlash \\
5. tab \t
6. back space\
7. menggunakan \n 
8. menggunakan \r
9. menggunakan \r\n
"""

print('ini adalah hari jum\'at, tolong persiapkan dari pagi')
print("D:\\Project\\Django-project")
print('muhaemin\t\troko, semakin jauh')
print('muhaemin\troko, kadang juga deket')
print('baris pertama, \nbaris kedua')
print('baris pertama, \rbaris kedua')
print('baris pertama, \r\nbaris kedua')

print(r"C:\new folder")


print('\n', 40*"=", '\n')
# Menggabunkan
data_1 = "aku"
data_2 = "harus"
data_3 = "bisa"
data_4 = "python"

data_lengkap = data_1 + data_2 + data_3 + data_4
print("gabungan kalimat: ", data_lengkap)

print('\n', 40*"=", '\n')
# Menghitung panjang string
panjang = len(data_lengkap)
print("panjang dari " + data_lengkap + "=" + str(panjang))

H = "H\n"
status = H in data_lengkap
print(H + "data di " + data_lengkap + "=" + str(status))


print('\n', 40*"=", '\n')
# Mengulang str
print("harus sukses" * 5)  # atua di balik juga bisa

# indexing
print("index ke-0: ", data_lengkap)

# item paling kecil / besar
print("paling kecil: " + min(data_lengkap))
print("paling kecil: " + max(data_lengkap))


# ascii code
ascii_code = ord(" ")
print("ascii code untuk spaci adalah: " + chr(ascii_code))
data = 1998
print("tahun untuk ascii 1998 adalah: " + chr(data))

# operasi didalam bentuk method
data = "orang sinting"
jumlah = data.count("i")
print("jumlah a pada " + data + "=" + str(jumlah))
