import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



#create random array
x=range(10, 201)
array= [x**2 for x in x]

def insertion_sort(array):

    for i in range(1, len(array)):

        key = array[i]

        j = i-1

        while j >= 0 and key < array[j]:

            array[j + 1] = array[j]
            j -= 1

            yield array

        array[j + 1] = key
        yield array

fig, ax = plt.subplots()
plt.bar(x,array)
plt.xlabel('Bars')
plt.ylabel('Values')

generator = insertion_sort(array)

# iteration = [0]

# def animate(array, iteration):
  
#     # setting the size of each bar equal
#     # to the value of the elements
#     for rect, val in zip(rects, A):
#         rect.set_height(val)
  
#     iteration[0] += 1
#     text.set_text("iterations : {}".format(iteration[0]))
  
  
anim = FuncAnimation(fig, func=None,
                     fargs=None, frames=generator, interval=50,
                     repeat=False)

plt.show()