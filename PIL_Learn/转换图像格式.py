# @Time    : 2019/12/3 8:42
# @Author  : Libuda
# @FileName: 转换图像格式.py
# @Software: PyCharm

from PIL import Image
import  os


def transImage(path):
    """
    转换图片格式
    :return:
    """
    for root,dir,files in os.walk(path):
        for infile in files:
            outfile = os.path.splitext(infile)[0]+".png"
            print(infile,outfile)
            if infile!=outfile:
                try:
                    #在这里要注意路径拼接 否则找不到相应的图片
                    Image.open(os.path.join(root,infile)).save(outfile)
                except Exception as e:
                    print("convert error",e)

def writeImage(path,write_path):
    """
    将指定文件夹下的内容写入指定文件中
    :param path:
    :param write_path:
    :return:
    """
    with open(write_path, 'w') as  f:
        for root, dirs, files in os.walk(write_path):
            for file in files:
                f.write(os.path.join(root, file) + '\n')


def deleteImage(image_path,delete_rule):
    """
    :param image_path: 删除图片路径
    :param delete_rule: delete_file = ['cs_1106_20191106_140956131_1.jpg', 'xs-1_1015_20191016_114122066_2.jpg']
    :return:
    """
    for root, dirs, file in os.walk(image_path):
        for name in file:
            print(name)
            if name in delete_rule:             #  填写规则
                os.remove(os.path.join(root, name))
                print("Delete File: " + os.path.join(root, name))


def getImagename(path,image_rule=None):
    """
    得到指定目录下指定格式的所有的图片名
    :param path:
    :return:
    """
    for root,dir,files in os.walk(path):
        for image in files:
            if image_rule:
                if image.endswith(image_rule):
                    print(os.path.join(root,image))

def getThumnailImage(image_pathl,size):
    """
    得到指定图片的缩略图
    size  元祖形式
    :param image_path:
    :return:
    """
    image = Image.open(image_path)
    #image.show()  原始图片展示
    image.thumbnail(size)
    image.show()

def cropImage(image_path,box):
    """
    从指定图片中裁剪指定区域
    :param image_path:
    :return:
    """
    if isinstance(box,tuple):
        image = Image.open(image_path)
        region = image.crop(box)
        region.show()
    else:
        print("输入边框应该是元组类型")

def transposeImage(image_path,jiaodu):
    """
    旋转图像
    :param image_path:
    :return:
    """
    image = Image.open(image_path)
    image = image.rotate(jiaodu)
    image.show()


def resizeImage(image_path,size):
    """
    调整图片大小
    :param image_path:
    :param size:
    :return:
    """
    image = Image.open(image_path)
    image = image.resize(size)
    image.show()


if __name__ == '__main__':
    path = r'C:\Users\lenovo\PycharmProjects\AI_learn\PIL_Learn\delete'
    image_path = r'C:\Users\lenovo\PycharmProjects\AI_learn\PIL_Learn\1.jpg'
    # box = (300,500,2500,1500)
    # cropImage(image_path,box)

    transposeImage(image_path,50)

