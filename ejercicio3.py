# autor: j. jesús Beltran
# Escribir una funcion recursiva que devuelva la suma de los primeros N enteros


def sumaDigitos(num) :
    s = 0 #suma de l0 digitos este numero
    while num > 0:
        s = s + num % 10
        num = num // 10
        return s

n = int(input ("cantidad de numeros:  ")) #cantidad de nuemros
sumaT = 0 #suma total
while n > 0:
    num = int(input("Numero:  "))
    sumaT = sumaT + sumaDigitos(num)
    n = n - 1

print(sumaT)


