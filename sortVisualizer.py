import random

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
from insertionSort import insertion_sort
from selectionsort import selection_sort
from matplotlib.widgets import Button

# create random array

x = random.randrange(30, 50)
array = [i for i in range(1, x + 1)]
random.shuffle(array)


generator = int(input('choose algorithm, 1:insertion, 2:selection  :'))
if generator == 1:
    insertion_sort(array)
elif generator == 2:
    selection_sort(array)

(fig, ax) = plt.subplots()
ax.set_title('SortVisualizer', fontsize=20)
plt.xlabel('Bars')
plt.ylabel('Values')

set_xlim = (0, x)
set_ylim = (1.2 * x)
text = ax.text(0.01, 0.95, '', transform=ax.transAxes)
iter = [0]
rect = ax.bar(range(len(array)), array)


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

# setting up writers object to capture animation in gif formart
# writer=writers['pillow']
# writer = writer(fps=30, metadata={'artist': 'Me'}, bitrate=1800)

# animation.save('Insertion Sort Visualization.gif')

plt.show()
