def devuelve_ciudades(*ciudades):
    for ciudad in ciudades:
        yield from ciudad

ciudades = devuelve_ciudades("Madrid", "Barcelona", "Berlin", "Paris")

print(next(ciudades))
print(next(ciudades))