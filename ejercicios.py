#Ejercicios - Codigo en Python
#Ejercicio 1 - Salario
# Solicitar datos
salario = float(input("Ingrese su salario mensual: "))
deudas = int(input("Ingrese el número de deudas activas: "))       
historial = input("Ingrese su historial crediticio (regular, bueno, excelente): ")

if (salario > 2500000 and deudas < 2):
    print("Tu crédito ha sido aprobado: cumple condiciones financieras.")
elif historial == "excelente":
    print("Tu crédito ha sido aprobado: historial crediticio excelente.")
else:
    print("Tu crédito ha sido rechazado: no cumple las condiciones.")



# Ejercicio 2 — IMC y riesgo cardiovascular
# Solicitar datos
peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))
edad = int(input("Ingrese su edad: "))

# Calcular IMC
imc = peso / (estatura ** 2)
print("Su IMC es: ", imc )
# Clasificación
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc <= 24.9:
    print("Clasificación: Normal")
elif 25 <= imc <= 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")    
    # Condición adicional
    if edad > 45:
        print("Riesgo cardiovascular alto")



# Ejercicio 3 — Validación de contraseña segura
contraseña = input("Ingrese la contraseña: ")
valida = True
tiene_mayuscula = False
tiene_numero = False
tiene_especial = False

# Verificar cada carácter
for c in contraseña:
    if c >= 'A' and c <= 'Z':
        tiene_mayuscula = True
    if c >= '0' and c <= '9':
        tiene_numero = True
    if c in "!@#$%&*":
        tiene_especial = True

# Validar longitud
if len(contraseña) < 8:
    print("Debe tener mínimo 8 caracteres.")
    valida = False

if not tiene_mayuscula:
    print("Debe contener al menos una mayúscula.")
    valida = False

if not tiene_numero:
    print("Debe contener al menos un número.")
    valida = False

if not tiene_especial:
    print("Debe contener al menos un carácter especial (!@#$%&*).")
    valida = False

# Resultado final
if valida:
    print("Contraseña válida ")
else:
    print("Contraseña no válida ")



#Ejercicio 4 - Clasificacion academica
creditos = int(input("Ingrese la cantidad de créditos aprobados: "))
promedio = float(input("Ingrese su promedio (0.0 a 5.0): "))

# Clasificación por año
if creditos <= 20:
    print("Clasificación: Primer año")
elif creditos <= 40:
    print("Clasificación: Segundo año")
elif creditos <= 60:
    print("Clasificación: Tercer año")
else:
    print("Clasificación: Cuarto año")

# Advertencia académica
if promedio < 3.0:
    print("Advertencia académica")

# Ejercicio 5 — Impuesto progresivo (versión básica)
ingreso = float(input("Ingrese su ingreso anual: "))
hijos = int(input("Ingrese el número de hijos: "))

# Determinar porcentaje
if ingreso <= 30000000:
    porcentaje = 5
elif ingreso <= 60000000:
    porcentaje = 10
elif ingreso <= 100000000:
    porcentaje = 20
else:
    porcentaje = 30

# Descuento si tiene más de 2 hijos
if hijos > 2:
    porcentaje = porcentaje - 2

# Calcular impuesto
impuesto = ingreso * porcentaje / 100

# Mostrar resultados
print("Porcentaje aplicado:", porcentaje, "%")
print("Valor final a pagar:", impuesto)



# Ejercicio 5 — Impuesto progresivo 

ingreso = float(input("Ingrese su ingreso anual: "))
hijos = int(input("Ingrese el número de hijos: "))

# Determinar porcentaje
if ingreso <= 30000000:
    porcentaje = 5
elif ingreso <= 60000000:
    porcentaje = 10
elif ingreso <= 100000000:
    porcentaje = 20
else:
    porcentaje = 30

# Descuento si tiene más de 2 hijos
if hijos > 2:
    porcentaje = porcentaje - 2

# Calcular impuesto
impuesto = ingreso * porcentaje / 100

# Mostrar resultados
print("Porcentaje aplicado:", porcentaje, "%")
print("Valor final a pagar:", impuesto)




# Ejercicio 6 — Validación y tipo de triángulo

a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))

# Validar si es triángulo
if a + b > c and a + c > b and b + c > a:
    
    print("Triángulo válido")
    
    # Clasificación
    if a == b and b == c:
        print("Tipo: Equilátero")
        
    elif a == b or a == c or b == c:
        print("Tipo: Isósceles")
        
    else:
        print("Tipo: Escaleno")

else:
    print("Triángulo inválido")



# Ejercicio 7 — Sistema de acceso multinivel

rol = input("Ingrese su rol (admin, profesor, estudiante): ")
estado = input("Ingrese su estado (activo, inactivo): ")

# Primero validar estado
if estado == "inactivo":
    print("Acceso denegado")

else:
    # Si está activo
    if rol == "admin":
        print("Acceso total")

    elif rol == "profesor":
        print("Acceso a notas y reportes")

    elif rol == "estudiante":
        print("Acceso a sus notas")

    else:
        print("Rol no válido")



# Ejercicio 8 — Evaluación de desempeño laboral

puntuacion = int(input("Ingrese la puntuación (0-100): "))
años = int(input("Ingrese los años en la empresa: "))

if puntuacion >= 90 and años > 5:
    print("Promoción inmediata")

elif puntuacion >= 80:
    print("Excelente")

elif puntuacion >= 70:
    print("Bueno")

elif puntuacion >= 60:
    print("Aceptable")

else:
    print("Bajo desempeño")



# Ejercicio 9 — Sistema de envíos

peso = float(input("Ingrese el peso del paquete: "))
tipo = input("Ingrese el tipo (nacional / internacional): ")
fragil = input("¿Es frágil? (si / no): ")

# Regla 1: Internacional y peso > 20
if tipo == "internacional" and peso > 20:
    print("Envío no permitido")

else:
    print("Envío permitido")

    # Regla 2: Frágil y peso > 10
    if fragil == "si" and peso > 10:
        print("Aplica recargo por fragilidad")

    # Regla 3: Nacional y peso < 5
    if tipo == "nacional" and peso < 5:
        print("Aplica tarifa reducida")



# Ejercicio 10 — Autenticación con intentos

usuario_correcto = "admin"
clave_correcta = "1234"

# Intento 1
usuario = input("Usuario: ")
clave = input("Contraseña: ")

if usuario == usuario_correcto and clave == clave_correcta:
    print("Acceso concedido")

else:
    print("Datos incorrectos. Intento 2")

    # Intento 2
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido")

    else:
        print("Datos incorrectos. Intento 3")

        # Intento 3
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")

        if usuario == usuario_correcto and clave == clave_correcta:
            print("Acceso concedido")

        else:
            print("Cuenta bloqueada")
