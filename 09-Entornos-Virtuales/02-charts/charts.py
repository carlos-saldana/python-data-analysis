# -*- coding: utf-8 -*-

#Importamos las librerías a emplear
import matplotlib.pyplot as plt

#Definimos una función para generar un pie
def generate_pie_chart():
    
    labels = ["A", "B", "C"]  #Etiquetas
    values = [200, 34, 120]   #Valores a tomar
    
    #Graficamos
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    
    #Guardamos la gráfica
    plt.savefig("pie.png")
    plt.close