import matplotlib.image as mimg
# from PIL import Image
import numpy as np
# import matplotlib.pyplot as mplt


def ft_load(path: str):
    """Loads and return a copy of the file"""
    try:
        ext_flag = False
        if path.endswith('.jpg') or path.endswith('.jpeg'):
            ext_flag = True
        assert ext_flag is True, "Wrong file extention"
        img = mimg.imread(path)
        print("The shape of image is:", img.shape)
        return np.copy(img)
    except AssertionError as msg:
        print("AssertionError", msg)
    except Exception as msg:
        print("ExceptionError", msg)

# def main():
#     # print(ft_load("landscape.jpg"))
#     print(ft_load("tester.py"))


# if __name__ == "__main__":
#     """Testing"""
#     main()
