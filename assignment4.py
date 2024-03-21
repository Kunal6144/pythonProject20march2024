import numpy as np

# Define matrix A
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

# Calculate the inverse matrix of A
A_inv = np.linalg.inv(A)

# Multiply A with its inverse matrix
product_AA_inv = np.dot(A, A_inv)

# Multiply the inverse matrix with A
product_A_invA = np.dot(A_inv, A)

# Print the results
print("Inverse matrix of A:")
print(A_inv)
print("\nProduct of A and its inverse matrix (A * A^-1):")
print(product_AA_inv)
print("\nProduct of the inverse matrix and A (A^-1 * A):")
print(product_A_invA)
