nota1 = float(input("Ingrese la nota 1 (15%): "))
nota2 = float(input("Ingrese la nota 2 (20%): "))
nota3 = float(input("Ingrese la nota 3 (25%): "))

porcentaje_acumulado = (nota1 * 0.15) + (nota2 * 0.20) + (nota3 * 0.25)
nota4_necesaria = (3.5 - porcentaje_acumulado) / 0.40

print("Para obtener una nota definitiva de 3.5, necesitas sacar en el examen final:")
print(nota4_necesaria)