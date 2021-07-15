import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

fig, ax = plt.subplots()
ax.plot(x_values, y_values, c=y_values, cmap=plt.cm.Blues, linewidth=3)

plt.show()
