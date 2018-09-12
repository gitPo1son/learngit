# -*- coding: utf-8 -*-
from wordcloud import WordCloud
from scipy.misc import imread
from os import path
from PIL import Image, ImageDraw, ImageFont
import codecs
import jieba
#import jieba.analyse as analyse
import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np



text = open('word.txt','r',encoding='UTF-8').read()
jieba.add_word('亚索')
cut_text = " ".join(jieba.cut(text))
d = path.dirname(__file__) # 当前文件文件夹所在目录
#color_mask = imread("亚索.jpg") # 读取背景图片
alice_coloring = np.array(Image.open('亚索.jpg'))


def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    with open('stopwords.txt') as f:
        str_text = f.read()
        # unicode_text = unicode(str_text, 'utf-8')  # 把str格式转成unicode格式
        f.close()  # stopwords文本中词的格式是'一词一行'
    for word in word_generator:
        if word.strip() not in str_text:
            words_list.append(word)
    return ' '.join(words_list)  # 注意是空格


# 绘制词云
def draw_wordcloud():
    #读入一个txt文件
    #text = open('word.txt','r',encoding='UTF-8').read()
    #结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
   # jieba.add_word('亚索')
    #cut_text = " ".join(jieba.cut(text))
    #d = path.dirname(__file__) # 当前文件文件夹所在目录
    #color_mask = imread("亚索啊啊啊啊.jpg") # 读取背景图片
    cloud = WordCloud(
        #设置字体，不指定就会出现乱码
        font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体,
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色
        background_color='black',
        #词云形状
        mask=alice_coloring,
        #允许最大词汇
        max_words=2000,
        #最大号字体
        max_font_size=42
    )

    text = stop_words(text)
    wc.generate(text)
    # 基于彩色图像生成相应彩色
    # image_colors = ImageColorGenerator(back_color)
    image_colors = ImageColorGenerator(alice_coloring)
    # 显示图片
    plt.imshow(wc)
    # 关闭坐标轴
    plt.axis('off')
    # 绘制词云
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis('off')
    # 保存图片
    wc.to_file('亚索11.png')




 #   word_cloud = cloud.generate(text) # 产生词云
  #  word_cloud.to_file("亚索44.jpg") #保存图片
    #  显示词云图片
 #   plt.imshow(word_cloud)
 #   plt.axis('off')
 #   plt.show()



if __name__ == '__main__':

    draw_wordcloud()