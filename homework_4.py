import numpy as np

def get_calibrate_coordinates(W, r, theta, alpha, f):

    W_h = homogeneous_points = np.vstack((W, np.ones((len(W[0]),))))

    A = np.eye(4)
    A[3, 2] = -1/f

    T = np.eye(4)
    T[0:3, 3] = -r

    R_theta = np.eye(4)
    R_theta[0:2, 0:2] = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

    R_alpha = np.eye(4)
    R_alpha[1:3, 1:3] = np.array([[np.cos(alpha), -np.sin(alpha)], [np.sin(alpha), np.cos(alpha)]])

    C_h = np.matmul(A, np.matmul(R_theta, np.matmul(R_alpha, np.matmul(T,W_h))))
    
    return C_h / C_h[-1]


r = np.array([0,0,0])
f = 1
W = np.array([[1.2, 1.2, 1.2, 1.2, 0.8, 0.8, 0.8, 0.8],
              [1.2, 1.2, 0.8, 0.8, 1.2, 1.2, 0.8, 0.8],
              [0.4, 0. , 0.4, 0. , 0.4, 0. , 0.4, 0. ]])

a_135 = 3*np.pi/4
a_0 = 0

# 1. pan = 135, tilt = 135
C_h = get_calibrate_coordinates(W, r, a_135, a_135, f)
print(C_h)

# 2. pan = 135, tilt = 0
C_h = get_calibrate_coordinates(W, r, a_135, a_0, f)
print(C_h)

# 3. pan = 0, tilt = 135
C_h = get_calibrate_coordinates(W, r, a_0, a_135, f)
print(C_h)

# 4. pan = 0, tilt = 0
C_h = get_calibrate_coordinates(W, r, a_0, a_0, f)
print(C_h)


















