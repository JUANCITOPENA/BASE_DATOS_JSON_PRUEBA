import pandas as pd
import json


df = pd.read_excel('datos_ventas_Version_Final_Muestra_20242000.xlsx', engine='openpyxl')

df['fecha_factura'] =df['fecha_factura'].astype(str)

data_dict = df.to_dict(orient='records')

json_data =json.dumps(data_dict, indent=4)

with open('datos.json', 'w') as json_file:
    json_file.write(json_data)    
    
print('EL Archivo Json se ha generado correctamente')    