from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
# import matplotlib.pyplot as mplt


def main():
    array = ft_load("landscape.jpg")
    ft_invert(array)
    # print(ft_invert.__doc__)
    # mplt.imshow(array, vmin=0, vmax=255)
    # mplt.show()
    # array = ft_load("landscape.jpg")
    ft_red(array)
    # print(ft_red.__doc__)
    # mplt.imshow(array, vmin=0, vmax=255)
    # mplt.show()
    # array = ft_load("landscape.jpg")
    ft_green(array)
    # print(ft_green.__doc__)
    # mplt.imshow(array, vmin=0, vmax=255)
    # mplt.show()
    # array = ft_load("landscape.jpg")
    ft_blue(array)
    # print(ft_blue.__doc__)
    # mplt.imshow(array, vmin=0, vmax=255)
    # mplt.show()
    ft_grey(array)
    # print(ft_grey.__doc__)
    # mplt.imshow(array, vmin=0, vmax=255)
    # mplt.show()


if __name__ == "__main__":
    """Testing"""
    main()
