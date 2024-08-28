# Solicitar la carga por teclado de dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Verificar si el primer número es mayor al segundo
if numero1 > numero2:
    suma = numero1 + numero2
    diferencia = numero1 - numero2
    print(f"La suma de los dos números es: {suma}")
    print(f"La diferencia de los dos números es: {diferencia}")
else:
    producto = numero1 * numero2
    if numero2 != 0:
        division = numero1 / numero2
        print(f"El producto de los dos números es: {producto}")
        print(f"La división del primero respecto al segundo es: {division}")
    else:
        print("No se puede realizar la división, el segundo número es 0.")
