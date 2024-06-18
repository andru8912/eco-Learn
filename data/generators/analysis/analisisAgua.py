import pandas as pd 
import matplotlib.pyplot as plt

from data.generators.generadorConsumoAbusivoAgua import generarDatosConsumoAbusivoAgua
from helpers.crearTablaHtml import crearTabla

def construirAguaDataFrame():
    datosAgua=generarDatosConsumoAbusivoAgua()
    
    #generamos el dataframe
    aguaDataFrame=pd.DataFrame(datosAgua,columns=['comuna', 'direccion', 'nombre', 'fecha', 'cantidad_litros'])
  
    
    crearTabla(aguaDataFrame,"datosAgua") 
    
    aguaDataFrame.replace('sin',pd.NA,inplace=True)
    
    filtroCantidaddadAguaBueno=aguaDataFrame.query("(cantidad_litros>=100)and(cantidad_litros<1000)").value_counts()
    filtroCantidaddadAguaAceptable=aguaDataFrame.query("(cantidad_litros>=1000)and(cantidad_litros<3000)").value_counts()
    filtroCantidaddadAguaMalo=aguaDataFrame.query("(cantidad_litros>=3000)and(cantidad_litros<10000)").value_counts()
    
    datosOrdenadosAgua = aguaDataFrame.groupby('comuna')['cantidad_litros'].mean()  # El error estaba aquí, corregido de 'comunna' a 'comuna'
    print(datosOrdenadosAgua)
   
    # Grafico la info
    plt.figure(figsize=(20, 10))  # Ajusta el tamaño de la figura
    datosOrdenadosAgua.plot(kind='bar', color='blue')
    plt.title("Indice de consumo abusivo de agua por comuna en Medellin", fontsize=22)
    plt.xlabel("Comuna", fontsize=17)
    plt.ylabel("Cantidad de litros", fontsize=17)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid(True)
    plt.savefig("img/calidadagua.png", format='png', dpi=300, bbox_inches='tight', pad_inches=0.1)
    
    
    
    
construirAguaDataFrame() 