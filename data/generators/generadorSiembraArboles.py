import random

def generarDatosSiembraArboles():
    
    listaDatos = []
    corregimientos = [
        'Corregimiento A', 'Corregimiento B', 'Corregimiento C', 
        'Corregimiento D', 'Corregimiento E', 'Corregimiento F'
    ]
    especies = ['Roble', 'Pino', 'Eucalipto', 'Acacia', 'Cedro']
    nombres = ['ana perez', 'jose jimeno', 'marco polo', 'martha lucrecia', 'karen andrea']
    correos = ['correo1@correo.com', 'correo2@correo.com', 'correo3@correo.com', 'correo4@correo.com', 'correo5@correo.com']
    fechas = ['2024-05-15', '2024-05-16', '2024-05-17']
    
    for i in range(1000):
        corregimiento = random.choice(corregimientos)
        hectareas_sembradas = round(random.uniform(0.1, 10.0), 2)  # Valores entre 0.1 y 10.0 hectáreas
        especie_sembrada = random.choice(especies)
        nombre = random.choice(nombres)
        fecha = random.choice(fechas)
        correo = random.choice(correos)
        
        encuesta = [corregimiento, hectareas_sembradas, especie_sembrada, nombre, fecha, correo]
        
        listaDatos.append(encuesta)
        
    return listaDatos
print (generarDatosSiembraArboles())