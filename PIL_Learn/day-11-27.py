# @Time    : 2019/11/27 10:42
# @Author  : Libuda
# @FileName: day-11-27.py
# @Software: PyCharm

from PIL import Image

#读取图片
image = Image.open("1.jpg")
#将图片转换为灰度图像
hui_image = image.convert("L")
#显示图片
hui_image.show()
