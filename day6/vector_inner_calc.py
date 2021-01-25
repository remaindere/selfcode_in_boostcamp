import numpy as np

vector_x = np.array([1,-1,1,-1], float)
vector_y = np.array([4,-4,4,-4], float)

def l1_norm(x) :
    x = abs(x)
    x = sum(x)
    return x

def l2_norm(x) :
    x = x ** 2
    x = np.sum(x)
    x = np.sqrt(x)
    return x

print(l2_norm(vector_x))
print(l2_norm(vector_y))
print(vector_x - vector_y)
print(l2_norm(vector_x-vector_y))

cos_theta = (l2_norm(vector_x)**2 + l2_norm(vector_y)**2 - l2_norm(vector_x - vector_y)**2) / (2 * (l2_norm(vector_x) * l2_norm(vector_y)))
print(cos_theta)
theta = np.arccos(cos_theta)
print(theta)
x_y_inner = l2_norm(vector_x)*l2_norm(vector_y)*cos_theta

print(x_y_inner)
x_y_defined_inner = (l2_norm(vector_x)**2 + l2_norm(vector_y)**2 - l2_norm(vector_x - vector_y)**2)/2
print(x_y_defined_inner)
print(np.inner(vector_x, vector_y))

X = np.array([[1,2,-3],
            [7,5,0],
            [-2,-1,2]], float)

X_inv = np.linalg.inv(X)

print(X@X_inv)
print(X_inv@X)

X2 = np.array([[1,0,1], [0,1,0]], float) # n<=m
X2_pinv = np.linalg.pinv(X2)
print(X2_pinv)
print(X2@X2_pinv) #A @ A^+
print(X2_pinv@X2)

X3 = np.array([[1,2],[3,4],[5,6]], float) # n>=m
X3_pinv = np.linalg.pinv(X3)
print(X3@X3_pinv)
print(X3_pinv@X3) #A^+ @ A

X4 = np.array([[1,0,1],[0,1,0],[1,1,0]], float)
X4_inv = np.linalg.inv(X4)
print(X4_inv)
print(X4@X4_inv)