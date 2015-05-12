# Dies ist nur ein Verlauf der Bearbeitung der Uebung
# in ipython

import numpy as np

import matplotlib.pyplot as plt

In [4]: x_min = -10.

In [5]: x_max = 10.

In [6]: x = np.random.uniform(x_m
x_max  x_min  

In [6]: x = np.random.uniform(x_min, x_max, 10)

In [7]: x
Out[7]: 
array([-4.86564111, -8.49550024, -5.20746281,  1.0401349 ,  1.36813848,
        8.97122107, -4.32292326, -1.05455792,  9.8835567 ,  6.94350457])

In [8]: m = 11

In [9]: x = np.random.uniform(x_min, x_max, m)

In [10]: x
Out[10]: 
array([ 1.09753351, -1.09333734, -3.6020064 , -5.64209291,  2.39763173,
        6.88430815,  1.7296714 , -8.62073638, -5.40026029,  0.34254698,
        0.75868902])

In [11]: a = 8.

In [12]: b = 5.

In [13]: y_without_noise = a * x + b

In [15]: y_without_noise
Out[15]: 
array([ 13.78026805,  -3.74669871, -23.81605118, -40.13674325,
        24.18105384,  60.07446524,  18.83737123, -63.965891  ,
       -38.20208231,   7.74037581,  11.06951216])

In [13]: y = y_without_noise + 9. * np.random.randn(11)

In [14]: plt.plot(x,y, "b*")
Out[14]: [<matplotlib.lines.Line2D at 0x107704410>]

In [15]: plt.show()

In [18]: for i in zip(x,y):
    print i
    ....:     
(-3.1354824101972056, -26.498458079467905)
(-0.20547809413092466, 9.1429763506612076)
(3.8035385313818928, 38.731569981140453)
(-3.7907215753599877, -39.656539927965618)
(-9.3533184124254571, -66.190971379744639)
(-9.6179298765262793, -78.991676235139565)
(-3.1175882577284781, -24.08390007686419)
(7.0947030602754637, 51.447905391821195)
(-9.2732368612890763, -68.727124050632014)
(-0.6830027406197221, 16.535361927501565)
(-9.6021702791140751, -77.110987668093486)

In [21]: def linear_hypothesis(theta_0, theta_1):
   ....:     return lambda x: theta_0 + theta_1 * x
   ....: 

In [22]: h = linear_hypothesis(theta_0 = 1., theta_1 = 2.)

In [23]: h(1)
Out[23]: 3.0

In [25]: h(2)
Out[25]: 5.0

In [26]: h( np.array([1., 2.]))
Out[26]: array([ 3.,  5.])

In [28]: def cost_function(x, y):
    assert type(x) == np.ndarray
    assert type(y) == np.ndarray
    assert len(x) == len(y)
    m = len(x)
    return lambda theta_0, theta_1: 1./(2. * m) * ((linear_hypothesis(theta_0, theta_1)(x) - y)**2).sum()
   ....: 

In [30]: squared_error_cost = cost_function

In [49]: ran = 100.

In [50]: paste
t0 = np.arange(a - ran, a + ran, ran * 0.05)
t1 = np.arange(b - ran, b + ran, ran * 0.05)

C = np.zeros([len(t0),len(t1)])
c =  squared_error_cost(x, y)

for i, t_0 in enumerate(t0):
  for j, t_1 in enumerate(t1):
    C[j][i] = c(t_0, t_1)

## -- End pasted text --

In [51]: T0, T1 = np.meshgrid(t0, t1)

In [52]: paste
plt.subplot(121)
plt.contour(T0, T1, C)
plt.xlabel('$\Theta_0$')
plt.ylabel('$\Theta_1$')
plt.title('Kostenfunktion')
## -- End pasted text --
Out[52]: <matplotlib.text.Text at 0x108354d50>

In [53]: plt.show()

In [54]: paste
def compute_new_theta(x, y, theta_0, theta_1, alpha):
    assert type(x) == np.ndarray
    assert type(y) == np.ndarray
    assert len(x) == len(y)
    m = len(x)
    temp_0 = theta_0 - alpha * (1. / m) * (theta_0 + theta_1 * x - y).sum()
    temp_1 = theta_1 - alpha * (1. / m) * ((theta_0 + theta_1 * x - y) * y).sum()
    return (temp_0, temp_1)

## -- End pasted text --


In [74]: theta_1 = 4.

In [75]: theta_0 = 4.

In [76]: theta_0, theta_1 = compute_new_theta(x, y, theta_0, theta_1, alpha = 0.0001)

In [77]: theta_0, theta_1 = compute_new_theta(x, y, theta_0, theta_1, alpha = 0.0001)

In [78]: theta_0, theta_1 = compute_new_theta(x, y, theta_0, theta_1, alpha = 0.0001)

In [79]: theta_0, theta_1 = compute_new_theta(x, y, theta_0, theta_1, alpha = 0.0001)

In [80]: theta_0, theta_1
Out[80]: (3.9945438435571687, 4.5352140761082502)

.
.
.

In [125]: theta_0, theta_1 = compute_new_theta(x, y, theta_0, theta_1, alpha = 0.0001)

In [126]: theta_0, theta_1
Out[126]: (3.9670718929219193, 7.3496602191753713)

In [127]: x_ = np.array([-10, 10])

In [130]: h_ = theta_0 + theta_1 * x_

In [131]: plt.plot(x_, h_, 'r-')
Out[131]: [<matplotlib.lines.Line2D at 0x10771cfd0>]

In [132]: plt.show()



