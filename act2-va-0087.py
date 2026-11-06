# Alonso López Garcia NC = 0087 | Fecha 06/11/2026
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Problema 7: Streaming (Plataforma, suscriptores en millones, opción gratis, lanzamiento)
# Crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 6 listas de Plataformas Streaming con 4 elementos por lista 
nfx = ['Netflix', 260, False, 2007]
dis = ['Disney+', 150, False, 2019]
spn = ['Spotify', 602, True, 2008]
ytb = ['YouTube Premium', 100, True, 2014]
hbo = ['Max', 95, False, 2020]
# Creamos una lista de listas 
lista_streaming = [nfx, dis, spn, ytb, hbo]
# print(lista_redes_sociales)
# Utilizar pandas para organizar la tabla (dataframe o marco de datos)
# A cada columna le ponemos su nombre 
df_streaming = pd.DataFrame(lista_streaming, columns=['Plataforma', 'Suscriptores (millones)', 'Opción Gratis', 'Año de Lanzamiento'])
print(df_streaming)
# Creamos el archivo CSV y lo guardamos en CSV }
df_streaming.to_csv("streaming.csv", index=False)
plt.plot(df_streaming["Plataforma"], df_streaming["Suscriptores (millones)"])
plt.title("Gráfica Plataformas Streaming NC 0087")
plt.xlabel("Nombre de las Plataformas de Streaming")
plt.ylabel("Cantidad de usuarios (millones)")
plt.show()
# Creamos una grafica de puntos
plt.scatter(df_streaming["Plataforma"], df_streaming["Suscriptores (millones)"])
plt.title("Gráfica de puntos Plataformas Streaming NC 0087")
plt.xlabel("Nombre de las Plataformas de Streaming")
plt.ylabel("Cantidad de usuarios (millones)")
plt.show()
# Creamos grafica de barras 
plt.bar(df_streaming["Plataforma"], df_streaming["Suscriptores (millones)"])
# Etiquetas y titulo 
plt.title("Gráfica de barras Plataformas Streaming NC 0087")
plt.xlabel("Nombre de las Plataformas de Streaming")
plt.ylabel("Cantidad de usuarios (millones)")
# Mostrar la gráfica 
plt.show()
# Ordenar la grafica de barras de manera descendente
# De la mas grande a la mas pequeña 
df_rs_ordenar = df_streaming.sort_values("Suscriptores (millones)", ascending = False)
plt.bar(df_rs_ordenar["Plataforma"], df_rs_ordenar["Suscriptores (millones)"])
plt.title("Gráfica de barras descendente Plataformas Streaming NC 0087")
plt.xlabel("Nombre de las Plataformas de Streaming")
plt.ylabel("Cantidad de usuarios (millones)")
plt.show()
# Darle color a la grafica
plt.bar(df_rs_ordenar["Plataforma"], df_rs_ordenar["Suscriptores (millones)"],
        color = ["b", "g", "c", "m", "y", "r"])
plt.title("Gráfica de barras descendente con color Plataformas Streaming NC 0087")
plt.xlabel("Nombre de las Plataformas de Streaming")
plt.ylabel("Cantidad de usuarios (millones)")
plt.show()
print(" ")
# Grafica pastel pie
# plt.plot(df_streaming["Nombre"], df_streaming["Cantidad"])
plt.pie(df_streaming["Suscriptores (millones)"],
        labels=df_streaming["Plataforma"])
plt.title("Gráfica Pastel Plataformas Streaming NC 0087")
plt.show()


print("Alonso Lopez Garcia NC = 0087 | Fecha 05/11/2026")