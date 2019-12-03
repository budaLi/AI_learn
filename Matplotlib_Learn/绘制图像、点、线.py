# @Time    : 2019/12/3 9:30
# @Author  : Libuda
# @FileName: 绘制图像、点、线.py
# @Software: PyCharm
from PIL import Image
from pylab import *

def drawPoint(image_path):
    image_point = array(Image.open(image_path))
    print("image_poine",image_point)
    #展示图片
    imshow(image_point)
    #一些点
    x=[100,100,400,400]
    y=[200,500,200,500]
    #画点
    plot(x,y,'r*')
    #按照点的顺序依次画线 必须两个点以上才有线
    #plot(x[:2],y[:2])
    plot(x,y)
    title("new image")
    #设置坐标轴不显示
    axis('off')
    #显示图片
    show()


if __name__ == '__main__':
    image_path = r'C:\Users\lenovo\PycharmProjects\AI_learn\Matplotlib_Learn\1.jpg'
    drawPoint(image_path)

