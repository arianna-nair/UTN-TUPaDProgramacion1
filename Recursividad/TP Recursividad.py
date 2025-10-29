#-----Actividad 1-----
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
numero = int(input("Ingrese un número: "))
for i in range(1, numero + 1):
    print(f"factorial de {i}= {factorial(i)}")

#-----Actividad 2-----
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
posicion = int(input("Ingrese la posición hasta donde mostrar Fibonacci: "))
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")

#-----Actividad 3-----
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = potencia(base, exponente)
print(f"\n{base}^{exponente} = {resultado}")

#-----Actividad 4-----
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
numero = int(input("Ingrese un número decimal: "))
if numero < 0:
    print("Por favor ingrese un número positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"\nEl número {numero} en binario es: {binario}")

#-----Actividad 5-----
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False
palabra = input("Ingrese una palabra: ").lower()
if es_palindromo(palabra):
    print(f"'{palabra}' SÍ es un palíndromo.")
else:
    print(f"'{palabra}' NO es un palíndromo.")

#-----Actividad 6-----
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"\nLa suma de los dígitos de {numero} es: {resultado}")

#-----Actividad 7-----
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
nivel_base = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(nivel_base)}")

#-----Actividad 8-----
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a contar (0-9): "))
resultado = contar_digito(numero, digito)
print(f"\nEl dígito {digito} aparece {resultado} veces en {numero}")