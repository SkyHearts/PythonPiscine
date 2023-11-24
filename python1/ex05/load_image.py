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
        # print("The shape of image is:", img.shape)
        # np_img = np.array(img)
        # zoom = np_img[100:500,450:850]
        # print("The shape of image is:", img.shape)
        # print("The zoom shape of image is:", zoom.shape)
        # # print(list(img))
        # imgplot = mplt.imshow(zoom)
        # mplt.show()
        return np.copy(img)
    except AssertionError as msg:
        print("AssertionError", msg)
    except Exception as msg:
        print("ExceptionError", msg)
