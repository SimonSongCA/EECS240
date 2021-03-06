# -*- coding: utf-8 -*-
"""EECS240_Proj2_Prob1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17y1z48BYJ5Mkiq5iUK_m4J-6BjliRJxc
"""

# Problem 1 - (a)
# Situation1:(α = 0.3)
import numpy
import matplotlib.pyplot as plt

# set up the limit for the problem
N = 300
# set up an all-zero variable
Y = numpy.zeros(N+1)
# the mean
mean = 0
# the alpha
α = 0.3
std = (1-α**2)**0.5
Y[0] = numpy.random.normal(mean, std, size=1)
# set up an initial iteration variable
i = 0
while i <= N-1:
    X = numpy.random.normal(mean, std, size=1)
    Y[i+1] = α*Y[i] + X
    i = i + 1
# plot the graph
plt.xlabel('Autoregressive Random Process')
plt.ylabel('Value')
plt.plot(Y)
plt.show()

# Problem 1 - (a)
# Situation2:(α = 0.95)
import numpy
import matplotlib.pyplot as plt

# set up the limit for the problem
N = 300
# set up an all-zero variable
Y = numpy.zeros(N+1)
# the mean
mean = 0
# the alpha
α = 0.95
std = (1-α**2)**0.5
Y[0] = numpy.random.normal(mean, std, size=1)
# set up an initial iteration variable
i = 0
while i <= N-1:
    X = numpy.random.normal(mean, std, size=1)
    Y[i+1] = α*Y[i] + X
    i = i + 1
# plot the graph
plt.xlabel('Autoregressive Random Process')
plt.ylabel('Value')
plt.plot(Y)
plt.show()

# Problem 1 - (b)
# a = 0.3
import numpy
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# set up the limit for the problem
N = 300
# set up an all-zero variable
Y = numpy.zeros(N+1)
# the mean
mean = 0
# the alpha
α = 0.3
std = (1-α**2)**0.5
Y[0] = numpy.random.normal(mean, std, size=1)
# set up an initial iteration variable
i = 0
while i <= N-1:
    X = numpy.random.normal(mean, std, size=1)
    Y[i+1] = α*Y[i] + X
    i = i + 1
# plot the graph
plot_acf(Y)
plt.show()

# Problem 1 - (b)
# a = 0.95
import numpy
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# set up the limit for the problem
N = 300
# set up an all-zero variable
Y = numpy.zeros(N+1)
# the mean
mean = 0
# the alpha
α = 0.95
# the standard deviation
std = (1-α**2)**0.5
Y[0] = numpy.random.normal(mean, std, size=1)
# set up an initial iteration variable
i = 0
while i <= N-1:
    X = numpy.random.normal(mean, std, size=1)
    Y[i+1] = α*Y[i] + X
    i = i + 1
# plot the graph
plot_acf(Y)
plt.show()

# Problem 1 - (c)
# a = 0.3
import numpy
import matplotlib.pyplot as plt
from scipy import signal

# set up the limit for the problem
N = 300
# set up an all-zero variable
Y = numpy.zeros(N+1)
# the mean
mean = 0
# the alpha
α = 0.3
# the standard deviation
std = (1-α**2)**0.5
Y[0] = numpy.random.normal(mean, std, size=1)
# set up an initial iteration variable
i = 0
while i <= N-1:
    X = numpy.random.normal(mean, std, size=1)
    Y[i+1] = α*Y[i] + X
    i = i + 1
# times of sampling
samp = 400
freqs, P_xx = signal.periodogram(Y, samp, scaling = 'density')
# plot the graph
plt.plot(freqs, P_xx)
plt.show()

# Problem 1 - (c)
# a = 0.95
import numpy
import matplotlib.pyplot as plt
from scipy import signal

# set up the limit for the problem
N = 300
# set up an all-zero variable
Y = numpy.zeros(N+1)
# the mean
mean = 0
# the alpha
α = 0.95
# the standard deviation
std = (1-α**2)**0.5
Y[0] = numpy.random.normal(mean, std, size=1)
# set up an initial iteration variable
i = 0
while i <= N-1:
    X = numpy.random.normal(mean, std, size=1)
    Y[i+1] = α*Y[i] + X
    i = i + 1
# times of sampling
samp = 400
freqs, P_xx = signal.periodogram(Y, samp, scaling = 'density')

# plot the graph
plt.plot(freqs, P_xx)
plt.show()