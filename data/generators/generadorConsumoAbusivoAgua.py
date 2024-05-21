import random

def generarDatosConsumoAbusivoAgua():
    
    listaDatos = []
    direcciones = [
        'Calle 1', 'Avenida 2', 'Carrera 3', 'Transversal 4', 'Diagonal 5',
        'Calle 6', 'Avenida 7', 'Carrera 8', 'Transversal 9', 'Diagonal 10'
    ]
    nombres = ['ana perez', 'jose jimeno', 'marco polo', 'martha lucrecia', 'karen andrea']
    fechas = ['2024-05-15', '2024-05-16', '2024-05-17']
    
    for i in range(1000):
        comuna = random.randint(1, 14)
        direccion = random.choice(direcciones)
        nombre = random.choice(nombres)
        fecha = random.choice(fechas)
        cantidad_litros = random.randint(100, 10000)  # Valores entre 100 y 10000 litros
        
        encuesta = [comuna, direccion, nombre, fecha, cantidad_litros]
        
        listaDatos.append(encuesta)
        
    return listaDatos
print (generarDatosConsumoAbusivoAgua())