import numpy as np

def vector_projection(A, B):
    dot_product = np.dot(A, B)
    magnitude_squared = np.dot(B, B)
    projection_scalar = dot_product / magnitude_squared
    projection_vector = projection_scalar * B
    return projection_vector

# Example vectors A and B
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Calculate the vector projection of A onto B
projection = vector_projection(A, B)
print("Vector projection of A onto B:", projection)
