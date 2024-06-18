import pandas as pd 
import matplotlib.pyplot as plt

from data.generators.generadorSiembraArboles import generarDatosSiembraArboles
from helpers.crearTablaHtml import crearTabla

def construirSiembraDataFrame():
    datosSiembraArboles=generarDatosSiembraArboles()
    
    #generamos el dataframe
    siembraDataFrame=pd.DataFrame(datosSiembraArboles,columns=['corregimiento', 'hectareas_sembradas', 'especie_sembrada', 'nombre', 'fecha', 'correo'])
    
    
    crearTabla(siembraDataFrame,"datosSiembraArboles") 
    
    siembraDataFrame.replace('sin',pd.NA,inplace=True)
    
    filtroSiembraBueno=siembraDataFrame.query("(hectareas_sembradas>=5)and(hectareas_sembradas<10)").value_counts()
    filtroSiembraAceptable=siembraDataFrame.query("(hectareas_sembradas>=3)and(hectareas_sembradas<5)").value_counts()
    filtroSiembraMalo=siembraDataFrame.query("(hectareas_sembradas>=1)and(hectareas_sembradas<3)").value_counts()
    
    datosOrdenadossiembra = siembraDataFrame.groupby('corregimiento')['hectareas_sembradas'].mean()  # El error estaba aquí, corregido de 'comunna' a 'comuna'
    print(datosOrdenadossiembra)
   
    # Grafico la info
    plt.figure(figsize=(20,10))
    datosOrdenadossiembra.plot(kind='bar', color='purple')
    plt.title("Indice de siembra de arboles por corregimiento ",fontsize=22 )
    plt.xlabel("corregimiento", fontsize=17)
    plt.ylabel("Hectareas sembradas", fontsize=17)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid(True)
    plt.savefig("./img/siembra.png", format='png', dpi=300, bbox_inches='tight', pad_inches=0.1)
    
   
    
construirSiembraDataFrame() 