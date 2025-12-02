"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    base = cargar_datos()
    graficos = graficar(base)
    guardar_datos(graficos)

def cargar_datos():    
    base = pd.read_csv("files/input/news.csv",index_col = 0)
    return base

def graficar(base):
    grafica = plt.figure()

    colores = {"Television":"dimgray",
                "Newspaper":"grey",
                "Internet": "tab:blue",
                "Radio":"lightgrey"}

    orden = {"Television":1,
                "Newspaper":1,
                "Internet": 2,
                "Radio":1}

    grosor = {"Television":2,
                "Newspaper":2,
                "Internet": 3,
                "Radio":2}

    for i in base.columns:
        plt.plot(base[i],
                    color = colores[i],
                    zorder = orden[i],
                    linewidth = grosor[i],
                    label = i)
            
    for i in base.columns:
        first_year = base.index[0]
        plt.scatter(
                x = first_year,
                y = base[i].loc[first_year],
                color = colores[i],
                zorder = orden[i]
            )

        plt.text(
                first_year-0.2,
                base[i].loc[first_year],
                i + " "+str(base[i][first_year]) + "%",
                ha = "right",
                va = "center",
                color = colores[i])

        last_year = base.index[-1]
        plt.scatter(
                x = last_year,
                y = base[i].loc[last_year],
                color = colores[i],
                zorder = orden[i]
            )

        plt.text(
            last_year+0.2,
                base[i].loc[last_year],
                str(base[i][last_year]) + "%",
                ha = "left",
                va = "center",
                color = colores[i])  

    plt.xticks(
            ticks = base.index,
            labels = base.index,
            ha = "center"
        )  

    plt.title("How people get their news", fontsize=16)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    return grafica
        
def guardar_datos(archivo):
        
    carpeta_salida="files/plots/"
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
    archivo.savefig("files/plots/news.png")