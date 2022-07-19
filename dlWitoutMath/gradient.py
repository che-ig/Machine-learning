import numpy as np
from matplotlib import pyplot as plt

function = lambda i: (i+10)*(i+2)*(i-5)*(i-11)

x = np.arange(-11, 13, 0.05)
y = [function(i) for i in x]

plt.figure(figsize=(9, 9))
plt.plot(x, y, )
plt.minorticks_on()
plt.grid(which="both")
plt.show()

def min_value_on_interval(function: callable, value: float, error: float =0.01) -> float:
    derivative_fun = 1
    last_value = value
    step = 0.0001
    while abs(derivative_fun) > error:
        derivative_fun = (function(last_value + step ) - function(last_value )) / step
        current_value = last_value - step * derivative_fun
        last_value = current_value
        
    return current_value


if __name__ == '__main__':
    print(min_value_on_interval(function, 0))