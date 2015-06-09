import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(-5., 5., 0.1)

def logistic_func(x):
    return 1 / (1 + math.e ** (-x))

y = logistic_func(x)

plt.plot(x, y)
plt.show()

x_min = -10.
x_max = 10.
m = 10

def logistic_hypothesis(theta):
    return lambda x: logistic_func(theta.T.dot(x))

theta =  theta = np.array([1.1, 2.0, -.9]) 

x1 = np.random.uniform(x_min, x_max, m)
x2 = np.random.uniform(x_min, x_max, m)
x3 = np.random.uniform(x_min, x_max, m)

X = np.column_stack([x1, x2, x3])

h = logistic_hypothesis(theta)

print(h(X.T))

