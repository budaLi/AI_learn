# @Time    : 2019/12/3 9:48
# @Author  : Libuda
# @FileName: 交互式标注.py
# @Software: PyCharm
from PIL import Image
from pylab import *
image_path=r'C:\Users\lenovo\PycharmProjects\AI_learn\Matplotlib_Learn\1.jpg'
im = array(Image.open(image_path))
imshow(im)
print('Please click 3 points')
point= ginput(3)
print('you clicked:', point)
show()
