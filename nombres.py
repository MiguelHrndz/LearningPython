def nombres(x): #2
    return x.split()

x = input("Introduzca nombre") #1

a = nombres(x)[0] #2
b = nombres(x)[1] #2

def cont(y) : #3
    return len(x)

print (f"Carácteres totales: {cont(x)}")

print (f"{a}, {len(a)}, {b},{len(b)}")






#1.- función 1: ingresar nombre y apellido 
# 2.- funcion1: separar nombre y apellido en 2 variables  
# 3.- funcion 2: construir una segunda función que cuente la cantidad de caracteres del parámetro ingresado  
# 4.- funcion1: debe imprimir el nombre y cantidad de caracteres, luego apellido y cantidad de caracteres
