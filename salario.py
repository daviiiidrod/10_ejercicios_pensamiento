salario = float(input("Ingrese su salario mensual: "))
deudas = int(input("Ingrese el número de deudas activas: "))
historial = input("Ingrese su historial crediticio (regular, bueno, excelente): ")

if (salario > 2500000 and deudas < 2):
    print("Tu crédito ha sido aprobado: cumple condiciones financieras.")
elif historial == "excelente":
    print("Tu crédito ha sido aprobado: historial crediticio excelente.")
else:
    print("Tu crédito ha sido rechazado: no cumple las condiciones.")
