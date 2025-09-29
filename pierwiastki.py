import math

#Podpunkt unos
suma = 0
for i in range(1, 11):
    suma += i**2
print(suma)

#Podpunkt dos
suma = 0
for i in range(100, 201):
    suma += math.sqrt(i)
print(suma)

#Podpunkt tres
suma = 0
for i in range(999, 9999):
    if i % 7 and i % 5 == 0:
        suma += math.sqrt(i)
print(suma)