import numpy as np
import matplotlib as plt

def linear_hypothesis(theta_0, theta_1):
    return lambda x: theta_0 + theta_1 * x

def cost_function(x, y):
    assert type(x) == np.ndarray
    assert type(y) == np.ndarray
    assert len(x) == len(y)
    m = len(x)
    return lambda theta_0, theta_1: 1./(2. * m) * ((linear_hypothesis(theta_0, theta_1)(x) - y)**2).sum()

def compute_new_theta(x, y, theta_0, theta_1, alpha):
    assert type(x) == np.ndarray
    assert type(y) == np.ndarray
    assert len(x) == len(y)
    m = len(x)
    temp_0 = theta_0 - alpha * (1. / m) * (theta_0 + theta_1 * x - y).sum()
    temp_1 = theta_1 - alpha * (1. / m) * ((theta_0 + theta_1 * x - y) * y).sum()
    return (temp_0, temp_1) 

x_min = -10.
x_max = 10.
m = 11

a = 8.

b = 5.

x = np.random.uniform(x_min, x_max, m)
y_without_noise = a * x + b


theta_0 = 1
theta_1 = 1

costs = []
delta = 0.5
alpha = 0.01
max_iterations = 1000


h = linear_hypothesis(theta_0, theta_1)
cf = costs