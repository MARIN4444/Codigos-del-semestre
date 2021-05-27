# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:54:10 2021

@author: marin
"""
# importar libreria
import pandas as pd

# Leer archivo excel
df_archivoExcel = pd.read_excel("ventas_productos_1.xlsx", index_col = "Producto")
df_archivosExcel = df_archivoExcel[:10].copy() # decir hasta cuantas filas queremos exportar o desde cuantas hasta tales
print(df_archivosExcel)

# Grafico Vertical
df_archivoExcel.plot(kind= "bar")

# Grafico Horizontal
df_archivoExcel.plot(kind= "barh")

df_archivoExcel.plot(kind= "barh", width=1) # cada grupo de barras ocupa todo el espacio