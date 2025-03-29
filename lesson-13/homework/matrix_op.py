import numpy as np

# 1. Create a vector with values ranging from 10 to 49.
vector = np.arange(10, 50)
print("Vector:", vector)

# 2. Create a 3x3 matrix with values ranging from 0 to 8.
matrix_3x3 = np.arange(9).reshape(3, 3)
print("3x3 Matrix:\n", matrix_3x3)

# 3. Create a 3x3 identity matrix.
identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)

# 4. Create a 3x3x3 array with random values.
random_3x3x3 = np.random.random((3, 3, 3))
print("3x3x3 Random Array:\n", random_3x3x3)

# 5. Create a 10x10 array with random values and find the min and max values.
random_10x10 = np.random.random((10, 10))
min_val, max_val = random_10x10.min(), random_10x10.max()
print("Min Value:", min_val, "Max Value:", max_val)

# 6. Create a random vector of size 30 and find the mean value.
random_vector = np.random.random(30)
mean_value = random_vector.mean()
print("Mean Value:", mean_value)

# 7. Normalize a 5x5 random matrix.
random_5x5 = np.random.random((5, 5))
normalized_matrix = (random_5x5 - np.min(random_5x5)) / (np.max(random_5x5) - np.min(random_5x5))
print("Normalized Matrix:\n", normalized_matrix)

# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
product_5x2 = np.dot(matrix_5x3, matrix_3x2)
print("Matrix Product (5x2):\n", product_5x2)

# 9. Compute the dot product of two 3x3 matrices.
matrix_A = np.random.random((3, 3))
matrix_B = np.random.random((3, 3))
dot_product = np.dot(matrix_A, matrix_B)
print("Dot Product:\n", dot_product)

# 10. Given a 4x4 matrix, find its transpose.
matrix_4x4 = np.random.random((4, 4))
transpose_matrix = matrix_4x4.T
print("Transpose:\n", transpose_matrix)

# 11. Create a 3x3 matrix and calculate its determinant.
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)
print("Determinant:", determinant)

# 12. Compute the matrix product (A . B) where A is (3x4) and B is (4x3).
A = np.random.random((3, 4))
B = np.random.random((4, 3))
matrix_product = np.dot(A, B)
print("Matrix Product (3x3):\n", matrix_product)

# 13. Compute the matrix-vector product for a 3x3 matrix and a 3-element column vector.
matrix_3x3_vec = np.random.random((3, 3))
vector_3 = np.random.random((3, 1))
vector_product = np.dot(matrix_3x3_vec, vector_3)
print("Matrix-Vector Product:\n", vector_product)

# 14. Solve the linear system (Ax = b) where A is a 3x3 matrix, and b is a 3x1 column vector.
A_sys = np.random.random((3, 3))
b_sys = np.random.random((3, 1))
x_solution = np.linalg.solve(A_sys, b_sys)
print("Solution x for Ax = b:\n", x_solution)

# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.
matrix_5x5 = np.random.random((5, 5))
row_sums = matrix_5x5.sum(axis=1)
col_sums = matrix_5x5.sum(axis=0)
print("Row-wise Sums:", row_sums)
print("Column-wise Sums:", col_sums)
