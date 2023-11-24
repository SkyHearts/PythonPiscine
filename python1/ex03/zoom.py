from load_image import ft_load
# import matplotlib.image as mimg
# from PIL import Image
import numpy as np
import matplotlib.pyplot as mplt


def rgb2gray(rgb):
    """return an aray with only one channel"""
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def zoom(img_array):
    """Uses slice to zoom"""
    np_img = np.array(img_array)
    sliced = np_img[100:500, 450:850]
    # sliced = np_img[100:500, 450:850, 0]
    return sliced


def main():
    """Runs the zoom function"""
    img = ft_load("animal.jpeg")
    # img_zoom = zoom(img)
    img_zoom = zoom(rgb2gray(img))
    # img_zoom = zoom(img.convert("L"))
    print(img)
    print("New shape after slicing:", img_zoom.shape)
    print(img_zoom)
    mplt.imshow(img_zoom, cmap=mplt.get_cmap('gray'), vmin=0, vmax=255)
    # mplt.imshow(img_zoom)
    mplt.show()


if __name__ == "__main__":
    """Testing"""
    main()
