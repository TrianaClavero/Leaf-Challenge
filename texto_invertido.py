# Desarrollar una función que reciba un texto e invierta el orden de las palabras siendo la
# última palabra la primera y la primera la última, debe devolver el texto invertido

def invertir_texto():
    texto = input("Ingrese un texto: ")
    palabras = texto.split()
    palabras_invertidas = palabras[::-1]
    print(" ".join(palabras_invertidas))

invertir_texto()
