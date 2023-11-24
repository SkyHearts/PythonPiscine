import numpy as np
import matplotlib.pyplot as mplt
# from typing import TypeVar
# from numpy.typing import NDArray


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts color channel of the original array, 255-r, 255-g, 255-b"""
    try:
        assert isinstance(array, np.ndarray) is True, "Wrong data type"
        # np_array = np.array(array)
        # dimesion = np_array.shape
        # row, column , color = dimesion
        # for i in range(row):
        #     for j in range(column):
        #         array[i][j][0] = 255 - array[i][j][0]
        #         array[i][j][1] = 255 - array[i][j][1]
        #         array[i][j][2] = 255 - array[i][j][2]
        new_array = 255 - array[:, :, :]
        # print(array)
        mplt.imshow(new_array, vmin=0, vmax=255)
        mplt.show()
        return array
    except AssertionError as msg:
        print("AssertionError", msg)


def ft_red(array) -> np.ndarray:
    """Zeroes the green and blue color channel of the original array"""
    try:
        assert isinstance(array, np.ndarray) is True, "Wrong data type"
        # np_array = np.array(array)
        # dimesion = np_array.shape
        # row, column , color = dimesion
        # for i in range(row):
        #     for j in range(column):
        #         array[i][j][1] = 0
        #         array[i][j][2] = 0
        new_array = np.copy(array)
        new_array[:, :, 1] = 0
        new_array[:, :, 2] = 0
        # print(array)
        mplt.imshow(new_array, vmin=0, vmax=255)
        mplt.show()
        return array
    except AssertionError as msg:
        print("AssertionError", msg)


def ft_green(array) -> np.ndarray:
    """Zeroes the red and blue color channel of the original array"""
    try:
        assert isinstance(array, np.ndarray) is True, "Wrong data type"
        new_array = np.copy(array)
        new_array[:, :, 0] = 0
        new_array[:, :, 2] = 0
        # print(array)
        mplt.imshow(new_array, vmin=0, vmax=255)
        mplt.show()
        return array
    except AssertionError as msg:
        print("AssertionError", msg)


def ft_blue(array) -> np.ndarray:
    """Zeroes the red and green color channel of the original array"""
    try:
        assert isinstance(array, np.ndarray) is True, "Wrong data type"
        new_array = np.copy(array)
        new_array[:, :, 0] = 0
        new_array[:, :, 1] = 0
        # print(array)
        mplt.imshow(new_array, vmin=0, vmax=255)
        mplt.show()
        return array
    except AssertionError as msg:
        print("AssertionError", msg)


def ft_grey(array) -> np.ndarray:
    """Mean the red,green and blue color channel of the original array"""
    try:
        assert isinstance(array, np.ndarray) is True, "Wrong data type"
        new_array = np.copy(array)
        new_array[:, :, :] = np.mean(new_array, axis=2, keepdims=True)
        # print(array)
        mplt.imshow(new_array, vmin=0, vmax=255)
        mplt.show()
        return array
    except AssertionError as msg:
        print("AssertionError", msg)
