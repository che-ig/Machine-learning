import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, lambdify

# Используем функционал sympy
sym_x = Symbol('x', real=True)
# sympy интерпретация функции.
f = sym_x**4 - 7 * sym_x**3 - 48 * sym_x**2 + 3 * sym_x - 50

# Получим выражение первой производной в виде формулы. В таком виде
# оно не подходит для расчетов.
derivative_f = f.diff(sym_x)
# Преобразуем производную в вид функции.
fun_derivative_f = lambdify(sym_x, derivative_f, 'numpy')

# Получим выражение второй производной в виде формулы.
derivative_2f = derivative_f.diff(sym_x)
# Преобразуем производную в вид функции.
fun_derivative_2f = lambdify(sym_x, derivative_2f, 'numpy')

# Сформируем аргумент функции.
x = np.linspace(-7, 12, 1000)

# Заполним данными значения производных для sympy варианта функции.
d1 = fun_derivative_f(x)
d2 = fun_derivative_2f(x)

# Классическая интерпретация функции.
y = x**4 - 7 * x**3 - 48 * x**2 + 3 * x - 50
# Ручное высчитывание производных.
dy = 4 * x**3 - 21 * x**2 - 96 * x + 3
d2y = 12 * x**2 - 42 * x - 96

# Создание полинома средствами numpy.
polynomial = np.poly1d([1, -7, -48, 3, 50])
# Высчитываем производные.средствами numpy.
deriv_1 = polynomial.deriv()
deriv_2 = deriv_1.deriv()
# Заполняем массивы производных данными.
data_deriv_1 = deriv_1(x)
data_deriv_2 = deriv_2(x)

fig, ax = plt.subplots(1, 3, figsize=(16, 16))
ax[0].plot(x, y, c='r')
ax[0].plot(x, dy, c='b')
ax[0].plot(x, d2y, c='g')

ax[1].plot(x, y, c='r')
ax[1].plot(x, d1, c='b')
ax[1].plot(x, d2, c='g')

ax[2].plot(x, polynomial(x), c='r', label='f(x)')
ax[2].plot(x, data_deriv_1, c='b', label='f\'(x)')
ax[2].plot(x, data_deriv_2, c='g', label='f\"(x)')

plt.legend(fontsize=14)
plt.grid()
plt.show()
