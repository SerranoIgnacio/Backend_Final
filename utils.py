
'''
Archivo con utilidades para la app
---------------------------
Autor: Ignacio Serrano
Version: 1.0

Descripcion:
En este programa se encuentran un graficador
'''

from cProfile import label
import io
import base64

import matplotlib
matplotlib.use('Agg')   # Para multi-thread, non-interactive backend (avoid run in main loop)
import matplotlib.pyplot as plt
# Para convertir matplotlib a imagen y luego a datos binarios
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg


def graficar(x, y):
    ''' 
        Crear el grafico que se desea mostrar en HTML
    '''
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.bar(x, y)
    ax.get_xaxis().set_visible(True)
    ax.set_facecolor('whitesmoke')
    ax.set_title("Turnos por Edad")
    ax.set_ylabel("Cantidad")
  #  ax.set_yticks(y)
    ax.set_xlabel("Edades")
 #   ax.set_xticks(x)

    image_html = io.BytesIO()
    FigureCanvas(fig).print_png(image_html)
    plt.close(fig) 
    return image_html