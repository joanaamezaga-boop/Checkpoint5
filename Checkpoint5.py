# Crear un bucle for. He añadido un condicional y el operador continue

ciudades = ["Donostia", "Madrid", "Bilbao", "Vitoria"]

for ciudad in ciudades:
    if ciudad == "Madrid":
        print(f"{ciudad} no está en el País Vasco")
        continue
    else:
        print(f"{ciudad} está en el País Vasco")
    

# Crear una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(num1, num2, num3):
    print(num1+num2+num3)

suma(25, 300, 5)

# Crear una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

lambda_suma = lambda num1, num2, num3: num1+num2+num3

print(lambda_suma(255, 52, 36))


# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
# nombre = 'Enrique'
# lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
nombre = 'Enrique'

if nombre in lista_nombre:
    print(f"{nombre} está en la lista")
else:
    print(f"{nombre} no está en la lista")














