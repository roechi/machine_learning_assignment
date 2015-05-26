import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
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

# Generate input dataset from random uniform distribution
x_min = -10.
x_max = 10.
m = 100

# First column does only contain ones
x0 = np.ones(m)
x1 = np.random.uniform(x_min, x_max, m)
x2 = np.random.uniform(x_min, x_max, m)

X = np.column_stack([x0, x1, x2])

# Set random theta
theta = np.random.uniform(x_min, x_max, 3)
# Generate set of results Y and apply gaussian noise for more realistic values
h = linear_hypothesis(theta)
Y = h(X) + np.random.normal(0, 10, m)

# Set constraint for gradient decent 
it = 500
alpha = 0.01

# Calculate gradient decent
res, theta = gradient_decent(alpha, theta, it, X, Y)

# And now for a whole lot of plotting
# First the convergence of the cost cost function
plt.figure(1)
plt.plot(range(0, it), res)
# And furthermore a plot of the hyperplane of the approximated function with the actual datapoints
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d'
xs = ys = np.arange(-10., 10., 1)
xs, ys = np.meshgrid(xs, ys)
XS = np.array([np.array([1., xx, yy]) for xx, yy in zip(np.ravel(xs), np.ravel(ys))])
zs = linear_hypothesis(theta)(XS)
zs = zs.reshape(xs.shape)
ax.plot_surface(xs, ys, zs, rstride=1, cstride=1, cmap=cm.gist_rainbow, linewidth=0, antialiased=True)
ax.scatter(x1, x2, zs=Y, zdir=u'z', s=20, c=u'r', depthshade=True)
plt.show()
