import numpy as np
import matplotlib as plt

x_min = -10.
x_max = 10.
m = 10

x1 = np.random.uniform(x_min, x_max, m)
x2 = np.random.uniform(x_min, x_max, m)

X = np.column_stack([x1, x2])

theta = np.random.uniform(x_min, x_max, 2)

def linear_hypothesis(theta):
    return lambda x: x.dot(theta)

h = linear_hypothesis(theta)

Y = h(X) + np.random.normal(-1, 1, m);

