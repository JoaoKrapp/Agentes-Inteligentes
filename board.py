import numpy as np
import matplotlib.pyplot as plt
import random


# Função que exibe o ambiente na tela
def exibir(matriz):
    posAPAx = 1
    posAPAy = 1

    # Altera o esquema de cores do ambiente
    plt.imshow(matriz, 'gray')
    plt.nipy_spectral()

    # Coloca o agente no ambiente
    plt.plot([posAPAy], [posAPAx], marker='o', color='r', ls='')

    plt.show(block=False)

    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(0.5)
    plt.clf()