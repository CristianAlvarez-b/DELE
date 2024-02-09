import numpy as np


def rotate_vector(vector, angle):
    # Convert angle to radians
    alpha = np.radians(angle)

    # Define rotation matrix
    rotation_matrix = np.array([[np.cos(alpha), -np.sin(alpha)],
                                [np.sin(alpha), np.cos(alpha)]])

    # Perform rotation using matrix multiplication
    rotated_vector = np.dot(rotation_matrix, vector)

    return rotated_vector


# Example vector
vector = np.array([3, 4])  # [v_x, v_y]
angle = 45  # Angle of rotation in degrees

# Rotate the vector
rotated_vector = rotate_vector(vector, angle)

print("Original vector:", vector)
print("Rotated vector:", rotated_vector)
