#algoritmo 11
def calcular_factura_agua(consumo_agua):
    cuota_fija = 6  # $6 para todos los segmentos
    tarifa_adicional = 0  # tarifa adicional por metro cúbico de agua
    
    # Segmento 1: consumo de 1 a 18 metros cúbicos de agua
    if consumo_agua <= 18:
        tarifa_adicional = 0
    # Segmento 2: consumo de 19 a 28 metros cúbicos de agua
    elif consumo_agua > 18 and consumo_agua <= 28:
        tarifa_adicional = 0.45 * (consumo_agua - 18)
    # Segmento 3: consumo de más de 28 metros cúbicos de agua
    elif consumo_agua > 28:
        tarifa_adicional = 0.45 * (28 - 18) + 0.65 * (consumo_agua - 28)
    
    total_factura = cuota_fija + tarifa_adicional
    
    return total_factura

# Pedir el consumo de agua al usuario
consumo_cliente = float(input("Ingrese el consumo de agua en metros cúbicos: "))

# Calcular la factura del cliente
factura_cliente = calcular_factura_agua(consumo_cliente)

# Imprimir la factura
print(f"El consumo de agua del cliente es: {consumo_cliente} m³")
print(f"La factura del cliente es: ${factura_cliente:.2f}")
