import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define sample data
y = np.array([5, 1, 6])
x = np.array([2, 5, 1])
ones_n = np.ones_like(y)

# Create the design matrix X
X_matrix = np.vstack([ones_n, x]).T

# Calculate the beta coefficients using the normal equation
try:
    beta_hat = np.linalg.inv(X_matrix.T @ X_matrix) @ X_matrix.T @ y
except np.linalg.LinAlgError:
    print("Matrix is not invertible. Please choose different vectors.")
    exit()

beta0_hat = beta_hat[0]
beta1_hat = beta_hat[1]

# Calculate the predicted vector y_hat
y_hat = beta0_hat * ones_n + beta1_hat * x

# Calculate the residual vector e
e = y - y_hat

# --- New coordinate system transformation ---
# The new basis vectors are aligned with x, 1_n, and the vector orthogonal to their plane.
# Use Gram-Schmidt to create an orthonormal basis.
u1 = x / np.linalg.norm(x)
u2_raw = ones_n - np.dot(ones_n, u1) * u1
u2 = u2_raw / np.linalg.norm(u2_raw)
u3 = e / np.linalg.norm(e)

# Project all vectors onto the new basis
def project_vector(v, basis):
    return np.array([np.dot(v, b) for b in basis])

y_proj = project_vector(y, [u1, u2, u3])
x_proj = project_vector(x, [u1, u2, u3])
ones_n_proj = project_vector(ones_n, [u1, u2, u3])
y_hat_proj = project_vector(y_hat, [u1, u2, u3])
e_proj = project_vector(e, [u1, u2, u3])
beta0_hat_ones_n_proj = project_vector(beta0_hat * ones_n, [u1, u2, u3])
beta1_hat_x_proj = project_vector(beta1_hat * x, [u1, u2, u3])

# Create the new 3D plot with the transformed coordinates
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the transformed vectors as arrows from the origin
ax.quiver(0, 0, 0, y_proj[0], y_proj[1], y_proj[2], color='blue', arrow_length_ratio=0.1, label='y')
ax.quiver(0, 0, 0, y_hat_proj[0], y_hat_proj[1], y_hat_proj[2], color='blue', linestyle='--', arrow_length_ratio=0.1, label='y_hat')
ax.quiver(y_hat_proj[0], y_hat_proj[1], y_hat_proj[2], e_proj[0], e_proj[1], e_proj[2], color='blue', arrow_length_ratio=0.1, label='e')
ax.quiver(0, 0, 0, beta0_hat_ones_n_proj[0], beta0_hat_ones_n_proj[1], beta0_hat_ones_n_proj[2], color='red', arrow_length_ratio=0.1, label='beta_0_hat * 1_n')
ax.quiver(beta0_hat_ones_n_proj[0], beta0_hat_ones_n_proj[1], beta0_hat_ones_n_proj[2], beta1_hat_x_proj[0], beta1_hat_x_proj[1], beta1_hat_x_proj[2], color='red', arrow_length_ratio=0.1, label='beta_1_hat * x')
ax.quiver(0, 0, 0, x_proj[0], x_proj[1], x_proj[2], color='black', arrow_length_ratio=0.1, label='x')
ax.quiver(0, 0, 0, ones_n_proj[0], ones_n_proj[1], ones_n_proj[2], color='black', arrow_length_ratio=0.1, label='1_n')

# Plot settings
max_lim = np.max(np.abs(y_proj)) * 1.2
ax.set_xlim([-max_lim, max_lim])
ax.set_ylim([-max_lim, max_lim])
ax.set_zlim([-max_lim, max_lim])
ax.set_xlabel('X-axis (Aligned with x)')
ax.set_ylabel('Y-axis (Aligned with 1_n)')
ax.set_zlabel('Z-axis (Aligned with e)')
ax.set_title('Geometric Interpretation of Linear Regression (Transformed Basis)')
ax.legend()
ax.grid(True)
plt.show()