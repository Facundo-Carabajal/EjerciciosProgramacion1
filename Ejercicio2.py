'''2. Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un
mensaje según el valor:
● 6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
● 4 y 5 ---> Aprobado, la nota es ...
● 1, 2 y 3 ---> Desaprobado, la nota es ...'''

#Investigue una funcion que me de un numero aleatorio.
import random

nota = random.randint(1, 10)

if nota >= 6:
    mensaje = f"Promoción directa, la nota es {nota}"
elif nota >= 4:
    mensaje = f"Aprobado, la nota es {nota}"
else:
    mensaje = f"Desaprobado, la nota es {nota}"

print(mensaje)
