import random

def generarDatosDeforestacion():
    
    listaDatos = []
    corregimientos = [
        'Corregimiento A', 'Corregimiento B', 'Corregimiento C', 
        'Corregimiento D', 'Corregimiento E', 'Corregimiento F'
    ]
    direcciones = [
        'Calle 1', 'Avenida 2', 'Carrera 3', 'Transversal 4', 'Diagonal 5',
        'Calle 6', 'Avenida 7', 'Carrera 8', 'Transversal 9', 'Diagonal 10'
    ]
    
    nombres = ['ana perez', 'jose jimeno', 'marco polo', 'martha lucrecia', 'karen andrea']
    fechas = ['2024-05-15', '2024-05-16', '2024-05-17']
    
    for i in range(1000):
        corregimiento = random.choice(corregimientos)
        hectareas_perdidas = round(random.uniform(0.1, 50.0), 2)  # Valores entre 0.1 y 50.0 hectáreas
        direccion = random.choice(direcciones)
        nombre = random.choice(nombres)
        fecha = random.choice(fechas)
        
        encuesta = [corregimiento, hectareas_perdidas, direccion, nombre, fecha]
        
        listaDatos.append(encuesta)
        
    return listaDatos
print (generarDatosDeforestacion())