import numpy as np
import matplotlib.pyplot as plt



#create random data
x=['A','B','C','D','E','F','G','I','j']
y= np.random.randint(low=5, high=100, size=9)

plt.bar(x,y)
plt.xlabel('Bars')
plt.ylabel('Values')
plt.show()