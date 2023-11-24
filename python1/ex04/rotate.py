from load_image import ft_load
import numpy as np
import matplotlib.pyplot as mplt


def rgb2gray(rgb):
    """return an aray with only one channel"""
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def zoom(img):
    """Uses slice to zoom"""
    np_img = np.array(img)
    sliced = np_img[100:500, 450:850]
    return sliced


def rotate(img):
    """Return an transposed array"""
    rez = [[img[j][i] for j in range(len(img))] for i in range(len(img[0]))]
    return np.array(rez)


def main():
    """Runs the rotate function"""
    img = ft_load("animal.jpeg")
    img_zoom = zoom(rgb2gray(img))
    # img_trans = img_zoom.transpose()
    img_trans = rotate(img_zoom)
    # img_trans = rotate(img_trans)
    print("The shape of image is:", img_zoom.shape)
    print(img)
    # print("New shape after Transpose:", img_trans.shape, type(img_trans))
    print("New shape after Transpose:", img_trans.shape)
    print(img_trans)
    mplt.imshow(img_trans, cmap=mplt.get_cmap('gray'), vmin=0, vmax=255)
    # mplt.imshow(img_zoom)
    mplt.show()


if __name__ == "__main__":
    """Testing"""
    main()
