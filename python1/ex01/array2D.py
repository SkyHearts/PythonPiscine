import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """slice the list given"""
    np_family = np.array(family)
    print("My shape is :", np_family.shape)
    sliced = np_family[start:end]
    print("My new shape is :", sliced.shape)
    return sliced.tolist()


# def main():
#     family = [[1.80, 78.4],
#               [2.15, 102.7],
#               [2.10, 98.5],
#               [1.88, 75.2]]
#     # print(family , type(family))
#     print(slice_me(family, 0, 2))
#     print(slice_me(family, 1, -2))


# if __name__ == "__main__":
#     """Testing"""
#     main()
