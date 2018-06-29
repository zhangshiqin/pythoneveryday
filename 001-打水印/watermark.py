
"""
作者：Isabella
时间：2018/6/13
题目：水印 —— 你是否想保护你图片的版权？在图片上加上标志或者文字来展示主权吧。

思路：
1. 打开图片
2. 创建水印文字（指定字体）
3. 叠加水印
4. 保存打了水印的图片

"""

from PIL import Image, ImageDraw, ImageFont

def add_watermark(image):

    # 打开原始图片
    oldpath = 'res/oldimg/'
    img = Image.open(oldpath + image)

    # 创建水印文字（指定字体）
    myfont = ImageFont.truetype('res/font/3270Medium.ttf', size = 30)
    fillcolor = "#fff"
    width, height = img.size

    # 给图片叠加水印
    draw = ImageDraw.Draw(img)
    draw.text((width-150, height-30), '@Isabella', font = myfont, fill = fillcolor)

    # 保存打了水印的图片
    newpath = 'res/newimg/marked_'
    file = newpath + image
    img.save(file, 'jpeg')
    print('Marked')

if __name__ == '__main__':
    image = 'water.jpg'
    add_watermark(image)


