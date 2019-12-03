# @Time    : 2019/12/3 10:43
# @Author  : Libuda
# @FileName: 直方图均衡化.py
# @Software: PyCharm

#直方图均衡化是指将一副图像的灰度直方图变平 使变换后的图像中每个灰度值的分布概率都相同
#目的是增强图像的对比度

# 如果一幅图像的灰度直方图几乎覆盖了整个灰度的取值范围，并且除了个别灰度值的个数较为突出，
# 整个灰度值分布近似于均匀分布，那么这幅图像就具有较大的灰度动态范围和较高的对比度，
# 同时图像的细节更为丰富。已经证明，仅仅依靠输入图像的直方图信息，就可以得到一个变换函数，
# 利用该变换函数可以将输入图像达到上述效果，该过程就是直方图均衡化。


from PIL import Image
from pylab import *
image_path=r'C:\Users\lenovo\PycharmProjects\AI_learn\Matplotlib_Learn\1.jpg'
im = array(Image.open(image_path).convert('L'))


def histeq(im,nbr_bins =256):
    """
    对一副灰度图像进行直方图均值化
    :param im:
    :param nbr_bins:
    :return:
    """
    #计算图像的直方图
    #histrgram 直方统计图函数
    # histogram(a, bins=10, range=None, weights=None, density=False);
    # a是待统计数据的数组；
    # bins指定统计的区间个数；
    # range是一个长度为2的元组，表示统计范围的最小值和最大值，默认值None，表示范围由数据的范围决定
    # weights为数组的每个元素指定了权值, histogram()
    # 会对区间中数组所对应的权值进行求和
    # density为True时，返回每个区间的概率密度；为False，返回每个区间中元素的个数
    print(im.shape)
    imhist, bins = histogram(im.flatten(),nbr_bins,density=False)
    print(imhist) #每个像素出现的次数
    print(bins)     #像素

    #累计分布函数 （cumulative distribution function，简写为 cdf，将像素值的范围映射到目标范围的归一化操作
    #cumsum 累加函数  https://blog.csdn.net/feng_jlin/article/details/82790746
    cdf = imhist.cumsum()

    #归一化
    cdf = 255*cdf /cdf[-1]
    #使用累计分布函数的线性插值  计算新的像素值
    #flatten 将图片多维向量转化为一维向量
    # interp  线性插值函数 https://blog.csdn.net/hfutdog/article/details/87386901
    im2  = interp(im.flatten(),bins[:-1],cdf)

    im2 = im2.reshape(im.shape)

    new_image = Image.fromarray(uint8(im2))
    # new_image.save("直方图均衡化图.jpg")
    new_image.show()


if __name__ == '__main__':
    histeq(im)