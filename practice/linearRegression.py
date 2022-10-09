import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

model = LinearRegression()
model.fit(x, y)

r2_score = model.score(x, y)

# coefficient of determination - R2
print(r2_score)

# Модель содержит атрибут intercept, который представляет собой
# коэффициент b0, и coef_, который представляет b1 коэффициент.
print('mode.intercept_ ', model.intercept_)
print('slope', model.coef_)

# Предскажем ответ
res = model.predict(x)

# Расчетный ответ
calculated_res = model.coef_ * np.ravel(x) + model.intercept_
print(res, calculated_res, sep='\n')
