import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

dir_veredas = '..\Data\arbolado-publico-lineal-2017-2018.csv'
dir_parques = '..\Data\arbolado-en-espacios-verdes.csv'

# Abro Datasets
df_parques = pd.read_csv(dir_parques)
df_veredas = pd.read_csv(dir_veredas)
df_parques.head()
df_veredas.head()

# Df tipuana
df_tipas_parques = df_parques[df_parques['nombre_gen']=='Tipuana'].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico']=='Tipuana tipu'].copy()

df_tipas_parques = df_tipas_parques[['diametro', 'altura_tot']].copy()
df_tipas_veredas = df_tipas_veredas[['diametro_altura_pecho', 'altura_arbol']].copy()

df_tipas_parques = df_tipas_parques.rename(columns={'altura_tot': 'altura'})
df_tipas_veredas = df_tipas_veredas.rename(columns={'diametro_altura_pecho': 'diametro', 'altura_arbol': 'altura'})

# Creo columna ambiente y relleno la celde como parque o vereda
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

# Unir los Datasets
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

# Boxplot Diametros
df_tipas.boxplot('diametro',by = 'ambiente')
plt.show()

# Alturas
df_tipas.boxplot('altura',by = 'ambiente')
plt.show()

# Renombar y Normalizar los nombres de datos y columnas
# Hacer una funcion que reciba los 2 df vereda y parque y nombre del arbol para filtrar los df por columna y agregar la de ambiente, que haga los boxplot