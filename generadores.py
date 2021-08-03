def generarPares(limite):
    num = 1
    lista = []

    while num < limite :
        yield num*2
        num += 1

generador = generarPares(10)

print(next(generador))
print("Aquí puede ir más código")
print(next(generador))
print("Aquí puede ir más código")
print(next(generador))
print("Aquí puede ir más código")
print(next(generador))
print("Aquí puede ir más código")