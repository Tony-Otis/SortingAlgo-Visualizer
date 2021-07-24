import random

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
from insertionSort import insertion_sort

# create random array

x = random.randrange(20, 50)
array = [i for i in range(1, x + 1)]
random.shuffle(array)


# def insertion_sort(array):

#     for i in range(1, len(array)):

#         key = array[i]

#         j = i - 1

#         while j >= 0 and key < array[j]:

#             array[j + 1] = array[j]
#             j -= 1

#             yield array

#         array[j + 1] = key

#         # array[i].set_color('r')

#         yield array


generator = insertion_sort(array)

(fig, ax) = plt.subplots()
ax.set_title('SortVisualizer', fontsize=20)
plt.xlabel('Bars')
plt.ylabel('Values')

set_xlim = (0, x)
set_ylim = 1.2 * x
text = ax.text(0.01, 0.95, '', transform=ax.transAxes)
iteration = [0]
rect = ax.bar(range(len(array)), array, align='edge')


def animate(array, rect, iteration):

    # setting the size of each bar equal
    # to the value of the arrays

    for (rect, val) in zip(rect, array):
        rect.set_height(val)

    iteration[0] += 1


animation = FuncAnimation(
    fig,
    func=animate,
    fargs=(rect, iteration),
    frames=generator,
    interval=4,
    repeat=False,
    )

#setting up writers object to capture animation in gif formart
# writer=writers['pillow']
# writer = writer(fps=30, metadata={'artist': 'Me'}, bitrate=1800)

# animation.save('Insertion Sort Visualization.gif')

plt.show()