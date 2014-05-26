# -*- coding: utf-8 -*-
from mpl_toolkits.axes_grid.axislines import SubplotZero
from matplotlib.transforms import BlendedGenericTransform
import matplotlib.pyplot as plt
import numpy


z=11
#グラフを何本引くかを設定します
#y=0があるので、偶数を入力すると左右対称になりません。

x = numpy.linspace(-5, 5, 1000)
#xの範囲を指定します。

def f(x, t):
    return 2 * t * x - t**2
#包絡線の元となる関数を設定します

if 1:
    fig = plt.figure(1)
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)

    ax.axhline(linewidth=1.7, color="black")
    ax.axvline(linewidth=1.7, color="black")

    plt.xticks([])
    plt.yticks([])
    plt.ylim([-30, 40])

    ax.text(0, 1.05, 'y', transform=BlendedGenericTransform(ax.transData, ax.transAxes), ha='center')
    ax.text(1.05, 0, 'x', transform=BlendedGenericTransform(ax.transAxes, ax.transData), va='center')

    for direction in ["xzero", "yzero"]:
        ax.axis[direction].set_axisline_style("-|>")
        ax.axis[direction].set_visible(True)

    for direction in ["left", "right", "bottom", "top"]:
        ax.axis[direction].set_visible(False)

        
    for a in range(-z/2 + 1, z/2 + 1):
        y = f(x, t=a)
        ax.plot(x, y, linewidth=1, color="black")

    plt.show()
    
