import numpy as np
import itertools

def combinations(array: np.array):
    states = array[1:,0]
    values = array[0, 1:]

    a = array[1:, 1:]
    allowed = []

    for s in range(len(states)):
        allowed.append([])
        for v in range(len(values)):
            if a[s][v]:
                allowed[s].append(v)
    return np.array(list(itertools.product(*(allowed[i] for i in range(len(states))))))


def convolution(array: np.array, kernel : np.array, flip=True):
    # Uses zero-padding
    # if flip:
    #     kernel = kernel.transpose()
    f_kernel = np.fliplr(np.flipud(kernel))

    row, col = array.shape
    kr, kc = kernel.shape

    center_row = int(np.floor(kr/2)) 
    center_col = int(np.floor(kr/2)) 

    sol = np.zeros(array.shape)
    dummy = np.zeros((row + 2*center_row, col + 2*center_row))
    dummy[center_row:-center_row,center_col:-center_col] = array

    for i in range(row):
        for j in range(col):
            sol[i][j] = np.sum(dummy[i:i+kr, j:j+kc] * f_kernel)

    return sol


kernel = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1],])

kernel6 = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1],])

image = np.array([[1, 7, 6, 3, 6],
                  [7, 6, 5, 6, 4],
                  [5, 4, 7, 7, 0],])


kernel2 = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0],])

image2 = np.array([[5, 0, 2, 3, 4],
                  [3, 2, 0, 5, 6],
                  [4, 6, 1, 1, 4],])

# print(convolution(image, kernel.transpose()))
# print(convolution(image, kernel))
print(convolution(image, kernel6))
# print(convolution(image2, kernel2.transpose()))


a = np.array([[None,    0, 1, 2, 3, 4],
              
              [0,       1, 1, 0, 1, 0],
              [1,       1, 1, 1, 0, 1],
              [2,       1, 0, 1, 0, 0]])


# l = combinations(a)
# print(l)
