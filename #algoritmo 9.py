#algoritmo 9

def convertir_moneda(valor, moneda_origen, moneda_destino):
    cotizaciones = {"USD": {"ARS": 98.73, "EUR": 0.84, "GBP": 0.73},
                    "ARS": {"USD": 0.01, "EUR": 0.008, "GBP": 0.007},
                    "EUR": {"USD": 1.19, "ARS": 120.25, "GBP": 0.86},
                    "GBP": {"USD": 1.38, "ARS": 139.86, "EUR": 1.16}}

    if moneda_origen == moneda_destino:
        return valor
    else:
        return valor * cotizaciones[moneda_origen][moneda_destino]


#(convertir_moneda(100, "USD", "ARS"))
    
#CONVERSOR DE LONGITUD

def convertir_longitud(valor, unidad_origen, unidad_destino):
    conversiones = {"metro": {"centimetro": 100, "kilometro": 0.001, "pie": 3.28084},
                    "centimetro": {"metro": 0.01, "kilometro": 0.00001, "pie": 0.0328084},
                    "kilometro": {"metro": 1000, "centimetro": 100000, "pie": 3280.84},
                    "pie": {"metro": 0.3048, "centimetro": 30.48, "kilometro": 0.0003048}}

    if unidad_origen == unidad_destino:
        return valor
    else:
        return valor * conversiones[unidad_origen][unidad_destino]

#(convertir_longitud(10, "metro", "pie"))  

#CONVERSOR DE MASA
def convertir_masa(valor, unidad_origen, unidad_destino):
    conversiones = {"gramo": {"kilogramo": 0.001, "miligramo": 1000, "libra": 0.00220462},
                    "kilogramo": {"gramo": 1000, "miligramo": 1000000, "libra": 2.20462},
                    "miligramo": {"gramo": 0.001, "kilogramo": 0.000001, "libra": 0.00000220462},
                    "libra": {"gramo": 453.592, "kilogramo": 0.453592, "miligramo": 453592}}

    if unidad_origen == unidad_destino:
        return valor
    else:
        return valor * conversiones[unidad_origen][unidad_destino]

#(convertir_masa(500, "gramo", "kilogramo"))  

#CONVERSOR DE ALMACENAMIENTO
def convertir_almacenamiento(valor, unidad_origen, unidad_destino):
    conversiones = {"bits": {"bytes": 0.125, "kilobits": 0.001, "megabits": 0.000001, "gigabits": 0.000000001, "terabits": 0.000000000001},
                    "bytes": {"bits": 8, "kilobits": 0.008, "megabits": 0.000008, "gigabits": 0.000000008, "terabits": 0.000000000008},
                    "kilobits": {"bits": 1000, "bytes": 125, "megabits": 0.001, "gigabits": 0.000001, "terabits": 0.000000001},
                    "megabits": {"bits": 1000000, "bytes": 125000, "kilobits": 1000, "gigabits": 0.001, "terabits": 0.000001},
                    "gigabits": {"bits": 1000000000, "bytes": 125000000, "kilobits": 1000000, "megabits": 1000, "terabits": 0.001},
                    "terabits": {"bits": 1000000000000, "bytes": 125000000000, "kilobits": 1000000000, "megabits": 1000000, "gigabits": 1000}}

    if unidad_origen == unidad_destino:
        return valor
    else:
        return valor * conversiones[unidad_origen][unidad_destino]

#(convertir_almacenamiento(1024, "bytes", "kilobits"))  


#CONVERSOR DE TIEMPO
def convertir_tiempo(valor, unidad_origen, unidad_destino):
    conversiones = {"segundo": {"minuto": 0.0166667, "hora": 0.000277778, "dia": 0.0000115741},
                    "minuto": {"segundo": 60, "hora": 0.0166667, "dia": 0.000694444},
                    "hora": {"segundo": 3600, "minuto": 60, "dia": 0.0416667},
                    "dia": {"segundo": 86400, "minuto": 1440, "hora": 24}}

    if unidad_origen == unidad_destino:
        return valor
    else:
        return valor * conversiones[unidad_origen][unidad_destino]

#(convertir_tiempo(3600, "segundo", "hora"))



#CONVERSOR DE VOLUMEN
def convertir_volumen(valor, unidad_origen, unidad_destino):
    conversiones = {"metro cubico": {"litro": 1000, "centimetro cubico": 1000000, "pie cubico": 35.3147},
                    "litro": {"metro cubico": 0.001, "centimetro cubico": 1000, "pie cubico": 0.0353147},
                    "centimetro cubico": {"metro cubico": 0.000001, "litro": 0.001, "pie cubico": 0.0000353147},
                    "pie cubico": {"metro cubico": 0.0283168, "litro": 28.3168, "centimetro cubico": 28316.8}}

    if unidad_origen == unidad_destino:
        return valor
    else:
        return valor * conversiones[unidad_origen][unidad_destino]

#(convertir_volumen(1, "metro cubico", "litro"))

#CONVERSOR DE AREA
def convertir_area(valor, unidad_origen, unidad_destino):
    conversiones = {"metro cuadrado": {"centimetro cuadrado": 10000, "kilometro cuadrado": 0.000001, "pie cuadrado": 10.7639},
                    "centimetro cuadrado": {"metro cuadrado": 0.0001, "kilometro cuadrado": 0.0000000001, "pie cuadrado": 0.00107639},
                    "kilometro cuadrado": {"metro cuadrado": 1000000, "centimetro cuadrado": 10000000000, "pie cuadrado": 10763910.4},
                    "pie cuadrado": {"metro cuadrado": 0.092903, "centimetro cuadrado": 929.03, "kilometro cuadrado": 0.0000003594}}

    if unidad_origen == unidad_destino:
        return valor
    else:
        return valor * conversiones[unidad_origen][unidad_destino]


#(convertir_area(100, "metro cuadrado", "pie cuadrado"))


#CONVERSOR DE Manzanas
def convertir_manzanas(valor, unidad_origen, unidad_destino):
    conversiones = {"manzana": {"metro cuadrado": 1000, "hectarea": 0.1},
                    "metro cuadrado": {"manzana": 0.001, "hectarea": 0.0001},
                    "hectarea": {"manzana": 10, "metro cuadrado": 10000}}

    if unidad_origen == unidad_destino:
        return valor
    else:
        return valor * conversiones[unidad_origen][unidad_destino]