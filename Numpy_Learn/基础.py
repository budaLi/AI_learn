# @Time    : 2019/12/3 10:01
# @Author  : Libuda
# @FileName: 基础.py
# @Software: PyCharm
from PIL import Image
from pylab import *

# 在先前的例子中，当载入图像时，我们通过调用 array() 方法将图像转换成 NumPy 的数组对象，
# 但当时并没有进行详细介绍。NumPy 中的数组对象是多维的，可以用来表示向量、矩阵和图像。
# 一个数组对象很像一个列表（或者是列表的列表），但是数组中所有的元素必须具有相同的数据类型。
# 除非创建数组对象时指定数据类型，否则数据类型会按照数据的类型自动确定。

image_path = r'C:\Users\lenovo\PycharmProjects\AI_learn\Matplotlib_Learn\1.jpg'

im = array(Image.open(image_path))
print(im.shape,im.dtype) # (3264, 2448, 3) uint8   图片的行列及颜色通道 数据类型 无符号8位整数