# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 19:14:12 2021

@author: lei
"""

from PIL import Image#第一行
'''
im=Image.open('C:\\superman.jpg')#第二行


print(im.format,im.size,im.mode)

'''
'''
im = Image.open('C:\\baotuan_join.gif')      # 读入一个GIF文件
try:
    im.save('picframe{:02d}.png'.format(im.tell()))
    while True:
        im.seek(im.tell()+1)
        im.save('picframe{:02d}.png'.format(im.tell()))
except:
    print("处理结束")
'''

'''
im = Image.open('C:\\calendar.jpg')
r, g, b = im.split()
om = Image.merge("RGB", (b, g, r))
om.save('supermanBGR.jpg')


from PIL import ImageFilter
im = Image.open('C:\\calendar.jpg')
om = im.filter(ImageFilter.CONTOUR)
om.save('supermanContour.jpg')


from PIL import ImageEnhance
im = Image.open('C:\\calendar.jpg')
om = ImageEnhance.Contrast(im)
om.enhance(20).save('supermancontrast.jpg')
'''

#e12.1DrawCharImage

ascii_char = list('"$%_&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-/+@<>i!;:,\^`.')
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 256 / len(ascii_char)
    return ascii_char[int(gray//unit)]
def main():
    im = Image.open('C:\\superman.jpg')
    WIDTH, HEIGHT = 100, 60
    im = im.resize((WIDTH, HEIGHT))
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    fo = open("pic_char.txt","w")
    fo.write(txt)
    fo.close()
main()
