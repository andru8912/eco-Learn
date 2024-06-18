import pandas as pd 
import matplotlib.pyplot as plt

from data.generators.generadorDeforestacion import generarDatosDeforestacion
from helpers.crearTablaHtml import crearTabla

def construirDeforestacionDataFrame():
    datosDeforestacion=generarDatosDeforestacion()
    
    #generamos el dataframe
    deforestacionDataFrame=pd.DataFrame(datosDeforestacion,columns=['corregimiento','hectareas_perdidas' , 'direccion', 'nombre', 'fecha'])
    
    
    crearTabla(deforestacionDataFrame,"datosDeforestacion") 
    
    deforestacionDataFrame.replace('sin',pd.NA,inplace=True)
    
    filtroDeforestacionBueno=deforestacionDataFrame.query("(hectareas_perdidas>=0.1)and(hectareas_perdidas<10)").value_counts()
    filtroDeforestacionAceptable=deforestacionDataFrame.query("(hectareas_perdidas>=10)and(hectareas_perdidas<30)").value_counts()
    filtroDeforestacionMalo=deforestacionDataFrame.query("(hectareas_perdidas>=30)and(hectareas_perdidas<50)").value_counts()
    
    datosOrdenadosdeforestacion = deforestacionDataFrame.groupby('corregimiento')['hectareas_perdidas'].mean()  
    print(datosOrdenadosdeforestacion)
    # Grafico la info
    plt.figure(figsize=(20,10))
    datosOrdenadosdeforestacion.plot(kind='bar', color='yellow')
    plt.title("Indice de hectareas perdidas por corregimiento",fontsize=22)
    plt.xlabel("corregimiento", fontsize=17)
    plt.ylabel("Hectareas perdidas", fontsize=17)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid(True)
    plt.savefig("./img/deforestacion.png", format='png', dpi=300, bbox_inches='tight', pad_inches=0.1)
    
    
    
    
    
construirDeforestacionDataFrame() 