import numpy as np

X = np.array([[1,1],[1,2],[2,2],[2,3]])
y = np.dot(X, np.array([1,2])) + 3

beta_gd = [4, 2, 5]
X_ = np.array([np.append(x,[1]) for x in X])
err = 0 
for t in range(1000):
    err = y - X_ @ beta_gd
    grad = -np.transpose(X_) @ err
    beta_gd = beta_gd - 0.01 * grad

print(beta_gd)