import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def linear_hypothesis(theta):
    return lambda x: x.dot(theta)

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

def gradient_decent(alpha, theta, nb_iterations, X, y):
    res = []
    j = cost_function(X, y);
    for x in range(0, nb_iterations):
        res.append(j(theta))
        theta = compute_new_theta(X, y, theta, alpha)
    return res, theta

x_min = -10.
x_max = 10.
m = 10

x1 = np.random.uniform(x_min, x_max, m)
x2 = np.random.uniform(x_min, x_max, m)

X = np.column_stack([x1, x2])

theta = np.random.normal(-10, 10, 2)

h = linear_hypothesis(theta)

Y = h(X) + np.random.normal(-5, 5, m)

plt.figure(1)
plt.subplot(111, projection='3d')

plt.scatter(x1, x2, zs=Y, zdir=u'z', s=20, c=u'r', depthshade=True)

it = 500
#theta = np.array([-1, 3])
alpha = 0.001
res, theta = gradient_decent(alpha, theta, it, X, Y)

plt.figure(2)
plt.plot(range(0, it), res)

fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')
xp = yp = range(-10, 10, 1)
XP, YP = np.meshgrid(xp, yp)
zp = np.array(linear_hypothesis(theta)(np.column_stack([xp, yp])))

ax.scatter(x1, x2, zs=linear_hypothesis(theta)(X), zdir=u'z', s=20, c=u'b', depthshade=True)
ax.scatter(x1, x2, zs=Y, zdir=u'z', s=20, c=u'r', depthshade=True)
plt.show()

