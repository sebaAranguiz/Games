<<<<<<< HEAD
#Este programa convierte numeros enteros a binarios:

n = input('Ingrese numero: ')

try:
    n = int(n)
except:
    print('Por favor ingresa solo numeros')
    quit()

#Bandera por si n es negativo
if n < 0:
    isNegative = True
    n = abs(n)
else:
    isNegative = False

#Ejecución
result = ''
if n == 0:
    result = '0'
while n > 0:
    result = str(n%2) + result
    n = n//2
if isNegative:
    result = '-' + result

print(result)
=======
#Este programa convierte numeros enteros a binarios:

n = input('Ingrese numero: ')

try:
    n = int(n)
except:
    print('Por favor ingresa solo numeros')
    quit()

#Bandera por si n es negativo
if n < 0:
    isNegative = True
    n = abs(n)
else:
    isNegative = False

#Ejecución
result = ''
if n == 0:
    result = '0'
while n > 0:
    result = str(n%2) + result
    n = n//2
if isNegative:
    result = '-' + result

print(result)
>>>>>>> add7d689aa54bdb9186681150c8266f7ce290fdc
