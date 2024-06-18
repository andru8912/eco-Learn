import random

def generarDatosCalidadAire():
    
    listaDatos=[]
    for i in range(1000):
        nombre=random.choice(['ana perez','jose jimeno','marco polo','martha lucrecia','karen andrea'])
        comuna=random.randint(1,14)
        ica=random.randint(10,80)
        fecha=random.choice(['2024-05-15','2024-05-16','2024-05-17','sin'])
        correo=random.choice(['correo1@correo.com','correo2@correo.com','correo3@correo.com',
        'correo4@correo.com','correo5@correo.com'])
        
        encuesta=[nombre,comuna,ica,fecha,correo]
        
        listaDatos.append(encuesta)
        
    return listaDatos
