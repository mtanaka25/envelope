# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

z = 11
#グラフを何本引くかを設定します
#y=0があるので、偶数を入力すると左右対称になりません。

def f(x, t):
    return 2 * t * x - t**2
#包絡線の元となる関数を設定します

#zの値と、fの形状を変化させれば、それっぽい図が出てくるようになっています。

def subplots():
    "Custom subplots with axes throught the origin"
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')

    return (fig, ax)


fig, ax = subplots()
x = np.linspace(-5, 5, 200)

for a in range(-z/2 + 1, z/2 + 1):
    y = f(x, t=a)
    ax.plot(x, y, 'b-', linewidth=2)

plt.show()
