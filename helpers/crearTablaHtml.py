def crearTabla(dataframe,nombreTabla):
    archivoHTML=dataframe.to_html()
    archivo=open(f"./tables/{nombreTabla}.html","w")
    archivo.write('''
            <html>
                <head>
                    <title>Tabla datos</title>
                </head> 
                <body>
                ''')
    archivo.write(archivoHTML)
    archivo.write(
                    '''
                
                </body> 
            </html>           
        ''')