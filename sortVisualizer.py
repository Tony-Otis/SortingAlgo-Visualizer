import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random



#create random array
x=int(input("Enter size"))
array= [i for i in range(1, x+1)]
random.shuffle(array)

def insertion_sort(array):

    for i in range(1, len(array)):

        key = array[i]

        j = i-1

        while j >= 0 and key < array[j]:

            array[j + 1] = array[j]
            j -= 1

            yield array

        array[j + 1] = key
        array[i].set_color('r')
        yield array

generator = insertion_sort(array)
#algorithm= 'Insertion Sort'

fig, ax = plt.subplots()
#plt.bar(x,array)
plt.xlabel('Bars')
plt.ylabel('Values')

set_xlim = (0, x)
set_ylim = (1.2* x)
text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
iteration = [0]
rects = ax.bar(range(len(array)), array, align = 'edge')

def animate(A, rects, iteration):
  
    # setting the size of each bar equal
    # to the value of the elements
    for rect, val in zip(rects, A):
        rect.set_height(val)
  
    iteration[0] += 1
    #text.set_text("iterations : {}".format(iteration[0]))
  
  
anim = FuncAnimation(fig, func=animate,
                     fargs=(rects, iteration), frames=generator, interval=50,
                     repeat=False)

plt.show()