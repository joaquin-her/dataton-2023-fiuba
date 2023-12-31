#Funciones utilizadas

from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    # Convertir las coordenadas de grados a radianes
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # Calcular las diferencias de latitud y longitud
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    # Calcular la distancia utilizando la fórmula de haversine
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    # Radio de la Tierra en kilómetros
    radius = 6371.0
    # Calcular la distancia
    distance = radius * c

    return distance

# Ejemplo de uso
lat_origen = 40.7128
lon_origen = -74.0060
lat_destino = 34.0522
lon_destino = -118.2437

distancia = haversine_distance(lat_origen, lon_origen, lat_destino, lon_destino)
print(f"La distancia entre los puntos es: {distancia:.2f} km")

def crearFormatID(fila):
    #La funcion devuelve la cadena concatenada de el indice con 3 cifras y el nombre
    id = str(fila[1]).zfill(3)
    return f"{str(id)} - {str(fila[2])}"
import unicodedata

def procesar_string(input_string):
    # Convertir a mayúsculas
    input_string = input_string.upper()
    # Eliminar tildes
    input_string = ''.join((c for c in unicodedata.normalize('NFD', input_string) if unicodedata.category(c) != 'Mn'))
    input_string.strip()
    input_string = input_string.replace("-", " - ")
    return input_string

def getLatitud(estacion):
    #print(estacion)
    return latitudEstaciones.get(estacion,None)

def getLongitud(estacion):
    #print(estacion)
    return longitudEstaciones.get(estacion,None)

def to_upper(nombre): 
    return nombre.upper() 
    
def convertir_a_entero(valor):
    if ',' in valor:
        # Eliminar la coma si está presente
        valor = valor.replace(',', '')
    # Convertir a entero
    return int(valor)

latitudEstaciones = {}
longitudEstaciones = {}
for index, row in estaciones_csv.iterrows(): 
    nombre_estacion = row['FormatId'].upper()
    latitud = row['Latitud']
    longitud = row['Longitud']
    if nombre_estacion not in latitudEstaciones:
        latitudEstaciones[nombre_estacion] = latitud
        longitudEstaciones[nombre_estacion] = longitud

-- ---- --
Viajes dentro del Barrio = CALCULATE(
    COUNTROWS('TablaViajes'),
    'TablaViajes'[EstacionInicio.Barrio] = "NombreDelBarrio",
    'TablaViajes'[EstacionFin.Barrio] = "NombreDelBarrio"
)

Viajes fuera del Barrio = CALCULATE(
    COUNTROWS('TablaViajes'),
    'TablaViajes'[EstacionInicio.Barrio] = "NombreDelBarrio",
    'TablaViajes'[EstacionFin.Barrio] <> "NombreDelBarrio"
)

Viajes dentro de la Comuna = CALCULATE(
    COUNTROWS('TablaViajes'),
    'TablaViajes'[EstacionInicio.Comuna] = "NombreDeLaComuna",
    'TablaViajes'[EstacionFin.Comuna] = "NombreDeLaComuna"
)

Viajes fuera de la Comuna = CALCULATE(
    COUNTROWS('TablaViajes'),
    'TablaViajes'[EstacionInicio.Comuna] <> "NombreDeLaComuna",
    'TablaViajes'[EstacionFin.Comuna] <> "NombreDeLaComuna"
)
.----- ------ -
''' Asumiendo que tienes una columna que indica el barrio (Barrio), otra columna para la comuna (Comuna), y una columna para la estación de destino (EstacionDestino) en tu conjunto de datos llamado Viajes, aquí hay un ejemplo general de cómo podrías hacer esto utilizando medidas calculadas en Power BI: '''
Viajes dentro del Barrio = 
CALCULATE(
    COUNTROWS('Viajes'),
    'Viajes'[Barrio] = SELECTEDVALUE('Viajes'[Barrio])
)

Viajes fuera del Barrio pero dentro de la Comuna = 
CALCULATE(
    COUNTROWS('Viajes'),
    'Viajes'[Barrio] <> SELECTEDVALUE('Viajes'[Barrio]),
    'Viajes'[Comuna] = SELECTEDVALUE('Viajes'[Comuna])
)

Viajes fuera de la Comuna = 
CALCULATE(
    COUNTROWS('Viajes'),
    'Viajes'[Comuna] <> SELECTEDVALUE('Viajes'[Comuna])
)
---------
Viajes con Origen en el Barrio y Destino dentro de la Comuna = 
CALCULATE(
    COUNTROWS('Viajes'),
    'Viajes'[BarrioOrigen] = SELECTEDVALUE('Viajes'[Barrio]) &&
    'Viajes'[ComunaDestino] = SELECTEDVALUE('Viajes'[Comuna])
)

Viajes con Origen en el Barrio y Destino fuera de la Comuna = 
CALCULATE(
    COUNTROWS('Viajes'),
    'Viajes'[BarrioOrigen] = SELECTEDVALUE('Viajes'[Barrio]) &&
    'Viajes'[ComunaDestino] <> SELECTEDVALUE('Viajes'[Comuna])
)