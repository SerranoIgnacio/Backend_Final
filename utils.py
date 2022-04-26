
'''
Archivo con utilidades para la app
---------------------------
Autor: Ignacio Serrano
Version: 1.0

Descripcion:
En este programa se encuentran un graficador
'''

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
    ax.get_xaxis().set_visible(False)

    image_html = io.BytesIO()
    FigureCanvas(fig).print_png(image_html)
    plt.close(fig) 
    return image_html