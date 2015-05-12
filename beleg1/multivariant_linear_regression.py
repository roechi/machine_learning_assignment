import numpy as np
import matplotlib as plt

x_min = -10.
x_max = 10.
m = 10

x1 = np.random.uniform(x_min, x_max, m)
x2 = np.random.uniform(x_min, x_max, m)

X = np.column_stack([x1, x2])

theta = np.random.uniform(x_min, x_max, m)

def linear_hypothesis(theta):
    return lambda x: x.T.dot(theta)

Y = h(X) + np.random.normal(0, 1, 2);