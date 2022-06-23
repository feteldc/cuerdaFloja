from time import sleep
from PIL import Image
import os
import numpy


def cortar_imagen(img_input, out_dir, d):
    """ 
    img_input:  nombre del archivo de imagen
    out_dir:    directorio donde su guardan las imagenes recortadas
    d:          dimensiones, en el estado actual el codigo solo corta en cuadrados perfectos,
                es decir, 2x2, 3x3, etc. (Puede modificarse ligeramente para cambiarlo)
    """
    # Separa el nombre de archivo de su extension para uso posterior
    name, ext = name, ext = os.path.splitext(img_input)

    # Abrir la imagen y la convierte en una array de numpy
    im = Image.open(img_input)
    im = numpy.array(im)

    # Definir dimensiones de corte
    M = im.shape[0]//d
    N = im.shape[1]//d

    # Separa la imagenes en partes de MxN pixeles
    tiles = [im[x:x+M,y:y+N] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]

    # Para definir los nombres de las imagenes de salida
    contador = 0
    for i in tiles:
        
        # Ignora una porcion si las dimensiones de esta son menores a lo esperado
        if i.shape[0] < im.shape[0]//d or i.shape[1] < im.shape[1]//d:
            continue
        # Crea imagen desde la array
        img = Image.fromarray(i, 'RGB')
        # Junta el output directory con un nombre de archivo formateado para guardar las porciones
        path = os.path.join(out_dir, f'{name}_{contador}{ext}')
        img.save(path)
        contador += 1

# Elmina los contenidos de la carpeta ingresada
def vaciar_carpeta(dir):
    """
    dir:    carpeta a vaciar
    """
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

if __name__ == "__main__":
    cortar_imagen('ef.png', 'screenshots', 3)
    sleep(5)
    vaciar_carpeta('screenshots')
