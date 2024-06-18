import pandas as pd 
import matplotlib.pyplot as plt

from data.generators.generadorAire import generarDatosCalidadAire
from helpers.crearTablaHtml import crearTabla

def construirAireDataFrame():
    datosAire=generarDatosCalidadAire()
    
    #generamos el dataframe
    aireDataFrame=pd.DataFrame(datosAire,columns=['nombre','comuna','ica','fecha','correo'])
    
    #generamos el recurso HTML
    #crearTabla(aireDataFrame,"datosAire")    
    
    
    #limpiando el dataframe
    #reemplazando valores
    aireDataFrame.replace('sin',pd.NA,inplace=True)
    
    
    
    #filtrar datos 
    #filtrar es aplicar condiciones logicas
    #que permitan analizar la informacion del DataFrame
    filtroCalidadAireBueno=aireDataFrame.query("(ica>=10)and(ica<40)").value_counts()
    filtroCalidadAireAceptable=aireDataFrame.query("(ica>=40)and(ica<50)").value_counts()
    filtroCalidadAireMalo=aireDataFrame.query("(ica>=50)and(ica<100)").value_counts()
    
    # Ordenando los datos para graficarlos
    datosOrdenadosAire = aireDataFrame.groupby('comuna')['ica'].mean()  # El error estaba aquí, corregido de 'comunna' a 'comuna'
    print(datosOrdenadosAire)
   
    # Grafico la info
    plt.figure(figsize=(20,10))
    datosOrdenadosAire.plot(kind='bar', color='green')
    plt.title("Indice de contaminacion del Aire por comuna en Medellin",fontsize=22)
    plt.xlabel("comuna", fontsize=17)
    plt.ylabel("ICA", fontsize=17)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid(True)
    plt.savefig("./img/calidadaire.png", format='png', dpi=300, bbox_inches='tight', pad_inches=0.1)
    
    
    

construirAireDataFrame()    