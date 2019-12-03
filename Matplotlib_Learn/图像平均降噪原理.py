# @Time    : 2019/12/3 11:39
# @Author  : Libuda
# @FileName: 图像平均降噪原理.py
# @Software: PyCharm
# https://blog.csdn.net/saltriver/article/details/78883872

# 前面提到，带有噪声的图像可以看作原始图像函数与噪声函数的和。
# f(x,y)=I(x,y)+Noise(x,y)

# 那么我们怎样从带有噪声的图像f(x, y)中去掉Noise得到I(x, y)呢？很自然的能想到，既然能加上噪声函数，那么把噪声函数减去不就行了。
#
# 是这样的，当然可以这样想。但是，绝大多数时候我们并不知道噪声函数是怎样的，即使知道噪声函数的表达式，但噪声函数一般都是随机的。
# 例如盐噪声就是随机的改变图像中的像素点，你并不知道到底改变的是哪些像素点！
#
# 那怎么办呢？我们知道图像带有如下天然的特性：图像中每个像素点的值与其旁边的像素点的值比较接近。这很显然。因为图像是现实世界的反映。
# 我们现实世界是连续的，除了对象边界外，每个对象反映在图像中，其覆盖的区域亮度都比较近似。
#
# 既然图像中的每个像素点的值与其旁边像素的值比较接近，如果一个像素点的值被噪声干扰，那么是否可以用其周边区域的像素平均值来代替这个像素点的值呢。
#
# 这就是平均操作：即把每个像素的值改变为其与领域像素组成区域的平均值。
#
# 领域是针对像素而言的，也就是像素点的周边区域像素。位于坐标(x, y)处的像素p有4个水平和垂直方向的相邻像素，这4个像素称为p的4领域，下图中标黑色的就是4领域。4领域的像素与p都只有1个单位距离。
from PIL import Image
from pylab import *
image_path=r'C:\Users\lenovo\PycharmProjects\AI_learn\Matplotlib_Learn\1.jpg'
im = array(Image.open(image_path).convert('L'))
image = Image.fromarray(im)
image.show()


def add_point(im):
    """
    添加盐噪点 随机将像素中的点变为白色
    :param im:
    :return:
    """
    x,y = im.shape
    x,y = [x-1,y-1]
    #更改百分之一次
    for i in range(int(0.01*x*y)):
        w = np.random.randint(x)
        h= np.random.randint(y)
        im[w][h] = 255  #255为白色

    image = Image.fromarray(im)
    image.show()

def remove_point(im):
    """
    根据图像平均原理进行去燥  该点像素值为其周边八个领域的平均值
    :param im:
    :return:
    """
    w,h = im.shape
    w,h = [w-1,h-1]
    for x in range(1,w):
        for y in range(1,h):
            if im[x][y]==255:   #白色点
                average_value=0
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        average_value+=im[i][j]
                im[x][y]=average_value//9
    new_image = Image.fromarray(im)
    new_image.show()


if __name__ == '__main__':
    add_point(im)
    remove_point(im)


