import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x1, x2, zs=Y, zdir=u'z', s=20, c=u'b', depthshade=True)
fig.show()

def cost_function(x, y):
    assert (len(x) == len(y))
    m = len(x)
    return lambda theta: 1./(2. * float(m)) * \
    ((linear_hypothesis(theta)(x) - y)**2).sum()

def compute_new_theta(x, y, theta, alpha):
    assert (len(x) == len(y))
    m = len(x)
    return (theta - alpha * (1./float(m) * \
    x.T.dot(linear_hypothesis(theta)(x) - y)))