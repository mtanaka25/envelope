import matplotlib.pyplot as plt
import numpy as np

z = 10
#グラフを何本引くかを設定します
#y=0は本数にカウントしていません

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
for a in range(-z/2, z/2 + 1):
   x = np.linspace(-5, 5, 200)
   y = f(x, t=a)
   ax.plot(x, y, 'b-', linewidth=2)
   ax.legend(loc='lower right')
plt.show()