cantidad = float(input("Ingrese la cantidad de productos: "))
precio_unitario = float(input("Ingrese el precio unitario sin IVA: "))
porcentaje_iva = float(input("Ingrese el porcentaje del IVA (por ejemplo, 19 para 19%): "))

subtotal = cantidad * precio_unitario
valor_iva = subtotal * (porcentaje_iva / 100)
subtotal_con_iva = subtotal + valor_iva
precio_unitario_con_iva = precio_unitario * (1 + porcentaje_iva / 100)
total = cantidad * precio_unitario_con_iva

print("Subtotal (sin IVA):", subtotal)
print("Valor del IVA:", valor_iva)
print("Subtotal con IVA:", subtotal_con_iva)
print("Total a pagar:", total)
