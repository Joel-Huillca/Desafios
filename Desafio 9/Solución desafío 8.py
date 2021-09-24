
listaCiudades = []
listaRegion = []
listaSucursales = []
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Agosto", "Septiembre", "Octubre", "Noviembre",
         "Diciembre"]

# Lectura de archivo sucursales.txt
arch = open("sucursales.txt", "r")
text = arch.readline().strip()
while text != "":
    partes = text.split(",")
    listaCiudades.append(partes[0])
    listaRegion.append(partes[1])
    listaSucursales.append(partes[2])
    text = arch.readline().strip()

# Ingreso de ventas por cada sucursal y mes correspondiente
matrizVentas = []
for i in range(len(listaSucursales)):
    listAuxVenta = []
    for j in range(12):
        venta = int(input("Ingrese las ventas de la Sucursal", listaSucursales[i], "en el mes de", meses[j]))
        listAuxVenta.append(venta)
    matrizVentas.append(listAuxVenta)

#REQUERIMIENTO A: Porcentaje de listaSucursales ubicadas en la Region de Antofagasta
cantidadAntofagasta = 0
for x in listaRegion:
    if x == "II Region de Antofagasta":
        cantidadAntofagasta += 1

print("El porcentaje de listaSucursales ubicadas en la region de Antofagasta es", cantidadAntofagasta / len(listaRegion))

#REQUERIMIENTO B: Promedio Total de Ventas
# Primero debemos conseguir la suma de ventas por cada sucursal, los resultados se almacenaran en la lista totalVentas
totalVentas = []

for fila in range(listaCiudades):
    suma = 0
    for columna in range(12):
        suma += matrizVentas[fila][columna]
    totalVentas.append(suma)

# Luego podemos calcular el promedio de ventas totales
sumaTotal = 0
for v in totalVentas:
    sumaTotal += v

print("El promedio del total de ventas es", sumaTotal / len(listaSucursales))

# REQUERIMIENTO C: Numero de la sucursal con menor ventas en el año
# Desde la lista totalVentas, podemos obtener esto
menor = 99999999
for n in totalVentas:
    if n < menor:
        menor = n
posicionMenor = totalVentas.index(menor)
print("La sucursal con menor ventas en el año es:", listaSucursales[posicionMenor], "y esta en la ciudad de",
      listaCiudades[posicionMenor])
print("con un monto de $", menor)

# REQUERIMIENTO D
# Promedio de Ventas para cada mes del año
promediosVentasMensuales = []

for x in range(len(meses)):
    sumaMes = 0
    for h in range(len(listaSucursales)):
        sumaMes += matrizVentas[h][x]
    promediosVentasMensuales.append(sumaMes / len(listaSucursales))

for p in range(len(meses)):
    print("El promedio de ventas para el mes de", meses[p], "es", promediosVentasMensuales[p])
