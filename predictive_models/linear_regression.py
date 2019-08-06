"""
linear regression is fitting a line to a set of observations
line can be used to predict unobserved observation values
"""

import numpy as np

import matplotlib.pyplot as plt

from scipy import stats

page_speeds = np.random.normal(3.0, 1.0, 1000)

purchase_amount = 100 - (page_speeds + np.random.normal(0, 0.1, 1000)) * 3

def linear_regression(page_speeds, purchase_amount):
    slope, intercept, r_value, p_value, stderr = stats.linregress(page_speeds, purchase_amount)

    return slope, intercept, r_value, p_value, stderr

def r_squared(r_value):
    return r_value ** 2

def predict(x, slope, intercept):
    return slope * x + intercept

def scatter_graph(x, y, fit_line):
    plt.scatter(page_speeds, purchase_amount)
    plt.plot(x, fit_line, c='r')
    plt.show()

slope, intercept, r_value, p_value, stderr = linear_regression(page_speeds, purchase_amount)

# r squared is a measure of the fit - ranges from 0 to 1
print('r squared: {:.3f}'.format(r_squared(r_value)))

fit_line = predict(page_speeds, slope, intercept)

scatter_graph(page_speeds, purchase_amount, fit_line)


