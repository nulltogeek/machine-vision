import numpy as np
import matplotlib.pyplot as plt

original_x = [2, 4, 4, 3, 2]
original_y = [1, 1, 3, 4, 3]

plt.plot(
    original_x + [original_x[0]],
    original_y + [original_y[0]],
    marker="o",
    label="Original Shape",
)

angle = -np.pi / 2

affine_matrix = np.array(
    [
        [np.cos(angle), -np.sin(angle), 3],
        [np.sin(angle), np.cos(angle), 1], 
        [0, 0, 1]
    ]
)


homogeneous_coords = np.vstack((original_x, original_y, np.ones(len(original_x))))
print(homogeneous_coords)

transformed_coords = np.dot(affine_matrix, homogeneous_coords)


transformed_x = transformed_coords[0, :]
transformed_y = transformed_coords[1, :]

plt.plot(
    transformed_x.tolist() + [transformed_x[0]],
    transformed_y.tolist() + [transformed_y[0]],
    marker="o",
    label="Transformed Shape",
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Original and Transformed Shapes")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
