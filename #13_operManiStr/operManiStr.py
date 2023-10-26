# Belajar operator manipulasi string (operator dalam method)
# merubah semua ke uppercase, lowercase  dan menggunakan is

# contoh 1
kalimat = "Aku sukaAA BangizZZ keeKKamuiszzSSS"
print('normal: ' + kalimat)

kalimat = kalimat.upper()
print('uper  : ' + kalimat)
kalimat = kalimat.lower()
print('lower : ' + kalimat)


# contoh 2 (is)
cek = kalimat.isupper()  # hasilnya boolean
print(kalimat + 'is upper: ' + str(cek))
cek = kalimat.islower()  # hasilnya boolean
print(kalimat + 'is lower: ' + str(cek))
