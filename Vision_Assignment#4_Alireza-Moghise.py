import numpy as np

matrix = np.array([[1, 1, 5, 6, 8], [2, 3, 5, 7, 1], [4, 5, 7, 1, 2], [8, 5, 1, 2, 5]])

delta_x = 1
delta_y = 1


def calculate_incidence_matrix(matrix, delta_x, delta_y):
    first_location_x_org = -1
    first_location_y_org = -1
    second_location_x_org = 0
    second_location_y_org = 0

    incidence_rows = incidence_cols = matrix.max()
    incidence_matrix = np.zeros((incidence_rows, incidence_cols))
    original_x, original_y = matrix.shape

    flg_brk = 0
    for x in range(original_x):
        if flg_brk == 1:
            break
        for y in range(original_y):

            first_location_x_org = x
            first_location_y_org = y
            second_location_x_org = x + delta_x
            second_location_y_org = y + delta_y

            if second_location_y_org >= 5:
                second_location_x_org = 0
                second_location_y_org = 0
                break

            print(
                first_location_x_org,
                first_location_y_org,
                second_location_x_org,
                second_location_y_org,
            )
            if second_location_x_org >= 4:
                flg_brk = 1
                break
            first_value = matrix[first_location_x_org][first_location_y_org]
            second_value = matrix[second_location_x_org][second_location_y_org]

            print(first_value, second_value)

            incidence_matrix[first_value][second_value] += 1
            # print(incidence_matrix)
    return incidence_matrix


res = calculate_incidence_matrix(matrix, delta_x, delta_y)
print(res)
