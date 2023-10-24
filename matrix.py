# Importamos las librerías necesarias
from tkinter import *
from random import randint

# Definimos las funciones que utilizaremos en el programa

# Función para mostrar la matriz en la ventana
def mostrar_matriz():
    for i in range(8):
        for j in range(8):
            # Convertimos los valores RGB de la matriz en un color hexadecimal
            color = '#%02x%02x%02x' % (matriz[i][j][0], matriz[i][j][1], matriz[i][j][2])
            # Creamos una celda en la ventana con el color correspondiente
            celda = Label(frame_matriz, bg=color, width=3, height=1)
            celda.grid(row=i, column=j)
            
# Función para mostrar la matriz en rojo
def mostrar_rojo():
    for i in range(8):
        for j in range(8):
            # Convertimos los valores RGB de la matriz en un color hexadecimal con el canal rojo al máximo
            color = '#%02x%02x%02x' % (matriz[i][j][0], 0, 0)
            # Creamos una celda en la ventana con el color correspondiente
            celda = Label(frame_matriz, bg=color, width=3, height=1)
            celda.grid(row=i, column=j)

# Función para mostrar la matriz en verde
def mostrar_verde():
    for i in range(8):
        for j in range(8):
            # Convertimos los valores RGB de la matriz en un color hexadecimal con el canal verde al máximo
            color = '#%02x%02x%02x' % (0, matriz[i][j][1], 0)
            # Creamos una celda en la ventana con el color correspondiente
            celda = Label(frame_matriz, bg=color, width=3, height=1)
            celda.grid(row=i, column=j)

# Función para mostrar la matriz en azul
def mostrar_azul():
    for i in range(8):
        for j in range(8):
            # Convertimos los valores RGB de la matriz en un color hexadecimal con el canal azul al máximo
            color = '#%02x%02x%02x' % (0, 0, matriz[i][j][2])
            # Creamos una celda en la ventana con el color correspondiente
            celda = Label(frame_matriz, bg=color, width=3, height=1)
            celda.grid(row=i, column=j)
            
# Función para mostrar la matriz en escala de grises
def mostrar_gris():
    for i in range(8):
        for j in range(8):
            # Calculamos el valor promedio de los canales RGB de la celda
            gris = (matriz[i][j][0] + matriz[i][j][1] + matriz[i][j][2]) // 3
            # Convertimos el valor promedio en un color hexadecimal en escala de grises
            color = '#%02x%02x%02x' % (gris, gris, gris)
            # Creamos una celda en la ventana con el color correspondiente
            celda = Label(frame_matriz, bg=color, width=3, height=1)
            celda.grid(row=i, column=j)
            
# Función para generar nuevos colores
def generar_colores():
    for i in range(8):
        for j in range(8):
            # Generamos valores aleatorios entre 0 y 255 para los canales RGB de la celda
            matriz[i][j][0] = randint(0, 255)
            matriz[i][j][1] = randint(0, 255)
            matriz[i][j][2] = randint(0, 255)
    # Mostramos la matriz en la ventana
    mostrar_matriz()

# Creamos la ventana principal
ventana = Tk()
ventana.title('Matriz de colores')

# Creamos el frame para la matriz
frame_matriz = Frame(ventana)
frame_matriz.grid(row=0, column=0)

# Creamos el frame para los botones
frame_botones = Frame(ventana)
frame_botones.grid(row=0, column=1)

# Creamos los botones y los ubicamos en el frame correspondiente
boton_mostrar = Button(frame_botones, text='Mostrar', command=mostrar_matriz)
boton_mostrar.grid(row=0, column=0)
boton_rojo = Button(frame_botones, text='Rojo', command=mostrar_rojo)
boton_rojo.grid(row=1, column=0)
boton_verde = Button(frame_botones, text='Verde', command=mostrar_verde)
boton_verde.grid(row=2, column=0)
boton_azul = Button(frame_botones, text='Azul', command=mostrar_azul)
boton_azul.grid(row=3, column=0)
boton_gris = Button(frame_botones, text='Gris', command=mostrar_gris)
boton_gris.grid(row=4, column=0)
boton_colores = Button(frame_botones, text='Generar colores', command=generar_colores)
boton_colores.grid(row=5, column=0)

# Creamos la matriz de 8x8 con valores aleatorios
matriz = []
for i in range(8):
    matriz.append([])
    for j in range(8):
        matriz[i].append([])
        for k in range(3):
            matriz[i][j].append(randint(0, 255))

# Mostramos la matriz en la ventana
mostrar_matriz()

# Ejecutamos el programa
ventana.mainloop()