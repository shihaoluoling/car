from numpy import *
from time import sleep
import matplotlib.pyplot as plt


def build_axes(bounds, buildings):
    plt.xlim(199)
    plt.ylim(119)
    fig1 = plt.figure((16, 8))
    axes1 = fig1.add_subplot()
    return axes1