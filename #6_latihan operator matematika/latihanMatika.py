# Belajar latihan konversi satuan temperatur
print("\nProgram Konveris Temperatur\n")

celcius = float(input("Masukan suhu dalam celius: "))
print("suhu adalah", celcius, "Celcius")

reamur = (4/5) * celcius
print("sudu adalah", reamur, "Reamur")

fahrenheit = ((9/5) * celcius) + 32
print("suhu adalah", fahrenheit, "Fahrenheit")

kelvin = celcius + 273
print("suhu adalah", kelvin, "Kelvin")


print("===============")
fahren = float(input("Masukan suhu fahrenheit: "))
print("suhu adalah", fahren, "Fahrenheit")

celcius = (5/9) * (fahren - 32)
kelvin = celcius + 273
print("suhu adalah", kelvin, "Kelvin")

print("===============")
kelvin = float(input("Masukan suhu kelvin: "))
print("suhu dalam Kelvin", kelvin, "Kelvin")

celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit", fahrenheit, "Fahrenheit")
