import pandas as pd 
import matplotlib.pyplot as plt

from data.generators.generadorRuidoAmbiental import generarDatosRuidoAmbiental
from helpers.crearTablaHtml import crearTabla

def construirRuidoDataFrame():
    datosRuidoAmbiental=generarDatosRuidoAmbiental()
    
    #generamos el dataframe
    RuidoDataFrame=pd.DataFrame(datosRuidoAmbiental,columns=['comuna', 'direccion', 'nombre', 'decibelios_diurnos', 'decibelios_nocturnos', 'fecha'])
    
      
    # Debugging: Print DataFrame structure
    print("DataFrame structure:")
    print(RuidoDataFrame.info())
    print("DataFrame head:")
    print(RuidoDataFrame.head())
    
    crearTabla(RuidoDataFrame,"datosRuidoAmbiental") 
    
    RuidoDataFrame.replace('sin',pd.NA,inplace=True)
    
    filtroDecibeliosBueno= RuidoDataFrame.query("(decibelios_diurnos>=50)and(decibelios_diurnos<60)").value_counts()
    filtroDecibeliosAceptable= RuidoDataFrame.query("(decibelios_diurnos>=60)and(decibelios_diurnos<80)").value_counts()
    filtroDecibeliosMalo= RuidoDataFrame.query("(decibelios_diurnos>=80)and(decibelios_diurnos<100)").value_counts()
    
    datosOrdenadosRuido = RuidoDataFrame.groupby('comuna')['decibelios_diurnos'].mean()  # El error estaba aquí, corregido de 'comunna' a 'comuna'
    print(datosOrdenadosRuido)
   
    # Grafico la info
    plt.figure(figsize=(20,20))
    datosOrdenadosRuido.plot(kind='bar', color='red')
    plt.title("Indice de decibelios diurnos por comuna en Medellin",fontsize=22)
    plt.xlabel("comuna", fontsize=17)
    plt.ylabel("Decibelios diurnos", fontsize=17)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid(True)
    plt.savefig("./img/ruido.png", format='png', dpi=300, bbox_inches='tight', pad_inches=0.1)
    
    
    
    
construirRuidoDataFrame() 