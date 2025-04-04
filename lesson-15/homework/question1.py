#Question 1
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 4*x + 4

x = np.linspace(-10, 10, 400)
y = f(x)

plt.plot(x, y, label=r"$f(x) = x^2 - 4x + 4$", color='b')

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x² - 4x + 4")

plt.grid(True)
plt.legend()

plt.show()

#Question 2
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 400)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y_sin, linestyle='-', marker='o', color='b', label=r'$\sin(x)$')  
plt.plot(x, y_cos, linestyle='--', marker='s', color='r', label=r'$\cos(x)$')  

plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title(r'Plot of sin(x) and cos(x)', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

#Question 3
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-2, 2, 400) 
x2 = np.linspace(0, 2*np.pi, 400) 
x3 = np.linspace(0, 2, 400)  
x4 = np.linspace(0, 5, 400) 

y1 = x1**3
y2 = np.sin(x2)
y3 = np.exp(x3)
y4 = np.log(x4 + 1)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(x1, y1, color='b')
axes[0, 0].set_title(r'$f(x) = x^3$')
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('f(x)')
axes[0, 0].grid(True)

axes[0, 1].plot(x2, y2, color='r')
axes[0, 1].set_title(r'$f(x) = \sin(x)$')
axes[0, 1].set_xlabel('x')
axes[0, 1].set_ylabel('f(x)')
axes[0, 1].grid(True)

axes[1, 0].plot(x3, y3, color='g')
axes[1, 0].set_title(r'$f(x) = e^x$')
axes[1, 0].set_xlabel('x')
axes[1, 0].set_ylabel('f(x)')
axes[1, 0].grid(True)

axes[1, 1].plot(x4, y4, color='m')
axes[1, 1].set_title(r'$f(x) = \log(x+1)$')
axes[1, 1].set_xlabel('x')
axes[1, 1].set_ylabel('f(x)')
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()

#Question 4
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

colors = np.random.rand(100)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, cmap='viridis', edgecolors='black', s=100)

plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)
plt.title('Scatter Plot of 100 Random Points', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.colorbar(label='Color Intensity') 

plt.show()

#Question 5
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)

plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Histogram of Normally Distributed Data (μ=0, σ=1)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

#Question 6
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

Z = np.cos(X**2 + Y**2)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

fig.colorbar(surf, ax=ax, shrink=0.6, aspect=10)

ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_zlabel('f(x, y)', fontsize=12)
ax.set_title(r'$f(x, y) = \cos(x^2 + y^2)$', fontsize=14)

plt.show()

#Question 7
import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.bar(products, sales, color=['blue', 'green', 'red', 'purple', 'orange'])

plt.title('Sales Data for Different Products')
plt.xlabel('Products')
plt.ylabel('Sales')

plt.show()

#Question 8
import matplotlib.pyplot as plt
import numpy as np

categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
data = np.array([[30, 40, 60, 70],  
                 [50, 60, 40, 60],  
                 [40, 50, 70, 50]])  


plt.bar(time_periods, data[0], label='Category A', color='blue')
plt.bar(time_periods, data[1], bottom=data[0], label='Category B', color='green')
plt.bar(time_periods, data[2], bottom=data[0] + data[1], label='Category C', color='red')

plt.title('Contribution of Categories Over Time')
plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.legend(title='Categories')

plt.show()

