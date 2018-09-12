# coding: utf-8
import jieba
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from os import path
from PIL import Image
import numpy as np

alice_coloring = np.array(Image.open('亚索09.jpg'))
wc = WordCloud(background_color='white',  # 背景颜色
               max_words=2000,  # 最大词数
               mask=alice_coloring,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=200,  # 显示字体的最大值
               stopwords=STOPWORDS.add('设置'),  # 使用内置的屏蔽词，再添加'苟利国'
               font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
               random_state=42,  # 为每个词返回一个PIL颜色
               #width=1000,  # 图片的宽
               #height=860  #图片的长
               )

# 添加自己的词库分词，比如添加'金三胖'到jieba词库后，当你处理的文本中含有金三胖这个词，
# 就会直接将'金三胖'当作一个词，而不会得到'金三'或'三胖'这样的词
jieba.add_word('亚索')
text = open('word.txt','r',encoding='UTF-8').read()  # 打开词源的文本文件

# 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
# 把你需要屏蔽的词全部放入一个stopwords文本文件里即可
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    with open('stopwords.txt') as f:
        str_text = f.read()
        f.close()  # stopwords文本中词的格式是'一词一行'
    for word in word_generator:
        if word.strip() not in str_text:
            words_list.append(word)
    return ' '.join(words_list)  # 注意是空格

text = stop_words(text)
wc.generate(text)
# 基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(alice_coloring)

plt.imshow(wc)  # 显示图片
plt.axis('off')  # 关闭坐标轴
plt.figure()  # 绘制词云
wc.to_file('亚索1111.png')

plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
plt.figure()
wc.to_file('亚索2222.png')

#plt.imshow(alice_coloring, cmap=plt.cm.gray,interpolation="bilinear")
#plt.axis("off")
#plt.show()
#wc.to_file('亚索333.png')  # 保存图片