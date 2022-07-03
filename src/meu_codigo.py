import matplotlib.pyplot as plt
import numpy as np


def minha_funcao():
    x = np.linspace(0, 2 * np.pi, 1030)
    plt.plot(x, np.sin(x))
    return plt


minha_funcao()
