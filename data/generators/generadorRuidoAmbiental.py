import random

def generarDatosRuidoAmbiental():
    
    listaDatos = []
    direcciones = [
        'Calle 1', 'Avenida 2', 'Carrera 3', 'Transversal 4', 'Diagonal 5',
        'Calle 6', 'Avenida 7', 'Carrera 8', 'Transversal 9', 'Diagonal 10'
    ]
    nombres = ['ana perez', 'jose jimeno', 'marco polo', 'martha lucrecia', 'karen andrea']
    correos = ['correo1@correo.com', 'correo2@correo.com', 'correo3@correo.com', 'correo4@correo.com', 'correo5@correo.com']
    fechas = ['2024-05-15', '2024-05-16', '2024-05-17']
    
    for i in range(1000):
        comuna = random.randint(1, 14)
        direccion = random.choice(direcciones)
        nombre = random.choice(nombres)
        decibelios_diurnos = random.randint(50, 100)
        decibelios_nocturnos = random.randint(40, 90)
        fecha = random.choice(fechas)
        
        encuesta = [comuna, direccion, nombre, decibelios_diurnos, decibelios_nocturnos, fecha]
        
        listaDatos.append(encuesta)
        
    return listaDatos
print (generarDatosRuidoAmbiental())
