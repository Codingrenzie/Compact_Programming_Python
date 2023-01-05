# Import standard modules
import numpy as np
import random
from numpy.linalg import matrix_rank


def integer_generator(num=10, random_arg=False, start=0, end=10):
    # Checks for parameter `random_arg``
    if not random_arg:
        # If parameter random_arg isn't there, generate set of integers with the parameter set by `num`
        return (i for i in range(num))
    else:
        # If parameter `random_arg` is there, generate 10 random integers
        return (random.randint(start, end) for i in range(num))


def generate_array(int_object=None, random_arg=False, m=1, n=None):
    # Checks for parameter `random_arg`
    if not random_arg:
        # If parameter random_arg isn't there, generate set of integers with the parameter set by `num`
        if int_object is not None:
            # Generate a 1D array using our iterable int object
            return np.fromiter(int_object, int)
    else:
        # If parameter random_arg isn't there, generate a random array 
        # having a length of parameter set by `aray_length`

        # Checks if array_legth is zero, 
        # if so use 1 insted of zero
        if (m == 0): m = 1
        if n is not None:
            return np.random.rand(m, n)
        else:
            return np.random.rand(m)


def compare_array(array_1, array_2):
    # Compares two arrays and return a boolean
    return np.array_equal(array_1, array_2)


def calculate_point_distance(vector):
    # Retrieve x values from the vector into a 2D array
    x = np.atleast_2d(vector[:, 0])
    # Retrieve y values from the vector into a 2D array
    y = np.atleast_2d(vector[:, 1])

    # Calculates the distance
    return np.sqrt((x - x.T) ** 2 + (y - y.T) ** 2)


def calculate_mean(array, axis_type, m, n):
    if (m > n):
        return None
    else:
        if axis_type == 'x':
            axis_num = 1
        if axis_type == 'y':
            axis_num = 0
        return np.mean(array, axis=axis_num)


def sort_by_column(array, n, col):
    if col - 1 >= n:
        return "Invalid input number for column, it should be less than n"
    else:
        return array[array[:, col].argsort()]


if __name__ == '__main__':
    # Question1
    print("_QUESTION-1_")
    print(generate_array(integer_generator(10)))

    # Question2
    print("_QUESTION-2_")
    # Generates an array with 10 integers
    array_temp = generate_array(integer_generator(10))
    # Randomly selects an integer from the list `array_temp`, 
    # which will be used as the length of the next array
    array_a_length = random.choice(array_temp)
    array_b_length = random.choice(array_temp)
    print(compare_array(generate_array(None, True, array_a_length), generate_array(None, True, array_b_length)))

    # Question3
    print("_QUESTION-3_")
    print(calculate_point_distance(generate_array(None, True, 100, 2)))

    # Question4
    print("_QUESTION-4_")
    m = 2
    n = 2
    mat = generate_array(None, True, m, n)
    mat_mean = calculate_mean(mat, 'x', m, n)
    if mat_mean is None:
        print("Invalid m n combination to calculate mean")
    else:
        print(mat - mat_mean)

    # Question5
    print("_QUESTION-5_")
    m = 2
    n = 2
    col = 1
    mat = generate_array(None, True, m, n)
    print(sort_by_column(mat, n, col))

    # Question6
    print("_QUESTION-6_")
    print(matrix_rank(generate_array(None, True, 3, 5)))

    # Question7
    print("_QUESTION-7_")
    mat = generate_array(None, True, 4, 4)
    block_size = 2
    print(np.add.reduceat(np.add.reduceat(mat, np.arange(0, mat.shape[0], block_size), axis=0),
                          np.arange(0, mat.shape[1], block_size), axis=1))
