total = float(input("Ingresa el total de la compra: "))
if total >= 100:
    descuento = total * 0.10
else:
    descuento = total * 0.05

total_final = total - descuento
print(f"El total con descuento es: {total_final}")
