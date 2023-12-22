# Code for multiple charts
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

a1,b1 = np.random.random(100), np.random.random(100)
a2,b2 = np.arange(100), np.random.random(100)

plt.figure(1)
plt.scatter(a1,b1, color="red")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.figure(2)
plt.plot(a2,b2)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

# Code for subplots
x = np.arange(100)
fig, axis=plt.subplots(2,2)
axis[0,0].plot(x,np.sin(x), color="green")
axis[0,0].set_title("Sine wave")

axis[0,1].plot(x,np.cos(x), color="blue")
axis[0,1].set_title("Cosine wave")

axis[1,0].plot(x,np.random.random(100), color="red")
axis[1,0].set_title("Random function")

axis[1,1].plot(x,np.log(x), color="orange")
axis[1,1].set_title("Log function")
fig.suptitle("The four plots")

plt.show()

# Code for 3D surface plot
axis = plt.axes(projection="3d")
x = np.arange(-7,7,0.5)
y = np.arange(-7,7,0.5)
X,Y = np.meshgrid(x,y)
Z = np.sin(X)*np.cos(Y)

axis.plot_surface(X,Y,Z)
axis.set_title("3D surface plot")

plt.show()
