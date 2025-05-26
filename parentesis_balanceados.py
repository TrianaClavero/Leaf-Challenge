# Desarrollar una función que reciba un texto e identifique que todos los paréntesis estén
# balanceados (chequear que siempre que se abra un paréntesis este se cierre), devolver
#True caso que así sea, False caso contrario
 
def parentesis_balanceados(cadena):
    pila = []
    for parentesis in cadena:
        if parentesis == "(":
            pila.append(parentesis)
        elif parentesis == ")":
            if not pila:
                return False
            pila.pop()
    return len(pila) == 0

cadena = input("Ingrese una cadena de paréntesis: ")

if parentesis_balanceados(cadena):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")
