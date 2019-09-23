import pytest
import image_analyser


def test_cat_in_pic():
    cat_pic_pth = '/home/pi/dev/cat_snapper/test_image.jpeg'
    assert image_analyser.item_in_pic('cat',cat_pic_pth) is True
