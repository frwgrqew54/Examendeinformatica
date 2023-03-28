#algoritmo 10

sueldo = float(input("Ingrese su sueldo mensual: "))

if sueldo <= 472:
    impuesto = 0
    cuota_fija = 0
elif sueldo <= 895.24:
    exceso = sueldo - 472
    impuesto = exceso * 0.1
    cuota_fija = 17.67
elif sueldo <= 2038.10:
    exceso = sueldo - 895.24
    impuesto = 42.53 + (exceso * 0.2)
    cuota_fija = 60
else:
    exceso = sueldo - 2038.10
    impuesto = 352.28 + (exceso * 0.3)
    cuota_fija = 288.57

iss = sueldo * 0.03
afp = sueldo * 0.0725
total_descuentos = iss + afp + impuesto + cuota_fija
sueldo_neto = sueldo - total_descuentos

print("Sueldo bruto: ${:.2f}".format(sueldo))
print("Impuesto sobre la renta: ${:.2f}".format(impuesto))
print("ISS: ${:.2f}".format(iss))
print("AFP: ${:.2f}".format(afp))
print("Cuota fija: ${:.2f}".format(cuota_fija))
print("Total descuentos: ${:.2f}".format(total_descuentos))
print("Sueldo neto: ${:.2f}".format(sueldo_neto))