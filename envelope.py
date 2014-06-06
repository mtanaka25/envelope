# -*- coding: utf-8 -*-
from mpl_toolkits.axes_grid.axislines import SubplotZero
from matplotlib.transforms import BlendedGenericTransform
import matplotlib.pyplot as plt
import numpy


z = 25
#グラフを何本引くかを設定します
#y=0があるので、偶数を入力すると左右対称になりません。

u = 1 #グラフ間隔の広さ
x = numpy.linspace(-10, 10, 2) #xの範囲を指定します。

ymin = -240 #グラフ縦方向の下限
ymax = 320 #グラフ縦方向の上限
#この２つはzと連動して適当に決まるようにしたい。

num = 1 
#保存するグラフデータのファイル名につける番号を入力します。
#保存したくない場合はNoneを書きます。

def f(x, t):
    return 2 * t * x - t**2
#包絡線の元となる関数を設定します

fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

ax.axhline(linewidth=1.7, color="black")
ax.axvline(linewidth=1.7, color="black")

plt.xticks([])
plt.yticks([])
plt.ylim([ymin, ymax])

ax.text(0, 1.05, '$y$', transform=BlendedGenericTransform(ax.transData, ax.transAxes), ha='center')
ax.text(1.05, 0, '$x$', transform=BlendedGenericTransform(ax.transAxes, ax.transData), va='center')

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

        
for a in range(-z/2 + 1, z/2 + 1):
    y = f(x, t = u * a)
    ax.plot(x, y, linewidth=1, color="black")

if num != None:
    plt.savefig('envelope' + str(num) + '.png')
    plt.savefig('envelope' + str(num) + '.pdf')

plt.show()