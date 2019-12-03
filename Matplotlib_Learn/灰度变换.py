# @Time    : 2019/12/3 10:26
# @Author  : Libuda
# @FileName: 灰度变换.py
# @Software: PyCharm

from PIL import Image
from pylab import *
image_path=r'C:\Users\lenovo\PycharmProjects\AI_learn\Matplotlib_Learn\1.jpg'
im = array(Image.open(image_path).convert('L'))

def imagetest1(im):
    """
    反向处理
    :return:
    """
    im = 255 - im
    new_image = Image.fromarray(uint8(im))
    new_image.save("test1.jpg")
    new_image.show()


    #如果只想查看 这俩必须一起用
    # imshow(im)
    # show()

def imagetest2(im):
    """
    将像素值映射到100-200
    :param im:
    :return:
    """
    im = (100.0/255.0)*im+100.0
    # imshow(im)
    new_image = Image.fromarray(uint8(im))
    new_image.save("test2.jpg")
    new_image.show()


if __name__ == '__main__':
    #如果你通过一些操作将uint8数据类型转换为其他数据类型 那么当你保存图片时要将数据类型转换回来
    imagetest1(im)
    imagetest2(im)



