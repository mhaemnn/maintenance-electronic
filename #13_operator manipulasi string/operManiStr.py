# Belajar operator manipulasi string (operator dalam method)
# merubah semua ke uppercase, lowercase  dan menggunakan is

# contoh 1
kalimat = "Aku sukaAA BangizZZ keeKKamszzSSS"
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


# contoh 3
cek = kalimat.isalpha()
print(kalimat + 'is alpha: ' + str(cek))

cek = kalimat.isalnum()
print(kalimat + 'is alnum: ' + str(cek))

cek = kalimat.isdecimal()
print(kalimat + 'is decimal: ' + str(cek))

cek = kalimat.isspace()
print(kalimat + 'is space: ' + str(cek))

cek = kalimat.istitle()
print(kalimat + 'is title: ' + str(cek))

# startswith dan endswith
start = "Python The Bast".startswith("Python")
print('start: ', str(start))

end = "Python The Bast".endswith("Bast")
print('end  : ', str(end))

# join & split
speack = ['I', 'Love', 'You']
combined = ' '.join(speack)
print(combined)


combined = "I Love You"
print(combined.split(' '))
