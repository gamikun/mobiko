from PIL import Image


def scale(image, size, iterate=False):
    new_image = image.thumbnail((size, size), Image.ANTIALIAS)
    return new_image