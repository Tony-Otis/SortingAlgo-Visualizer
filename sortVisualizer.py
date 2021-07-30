import random

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers

from insertionSort import insertion_sort
from heapsort import heapSort
from selectionsort import selection_sort

# create random array

x = random.randrange(30, 50)
array = [i for i in range(1, x + 1)]
random.shuffle(array)



generator = int(input('choose algorith, 1:insertion, 2:selection, 3:heap_sort  :'))
if generator == 1:
    generator=insertion_sort(array)
elif generator == 2:
    generator=selection_sort(array)
elif generator == 3:
    generator=heapSort(array)

(fig, ax) = plt.subplots()
ax.set_title('Heap Sort', fontsize=20)
plt.xlabel('Bars')
plt.ylabel('Values')

set_xlim = (0, x)
set_ylim = (1.2 * x)
iter = [0]
rect = ax.bar(range(len(array)), array)
# rect[1].set_color('red')


def animate(array, rect, iter):

    # setting the size of each bar equal
    # to the value of the arrays

    for (rect, val) in zip(rect, array):
        rect.set_height(val)

    iter[0] += 1


animation = FuncAnimation(
    fig,
    func=animate,
    fargs=(rect, iter),
    frames=generator,
    interval=4,
    repeat=False,
)

save = input('Save Animation? (y|n) :')
if save != 'y':
    save=False
# setting up writers object to capture animation in gif formart
writer=writers['pillow']
writer = writer(fps=30, metadata={'artist': 'Me'}, bitrate=1800)

if save:
    animation.save('heapsort.gif')

plt.show()
