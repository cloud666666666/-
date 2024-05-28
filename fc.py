# -*- coding:utf-8 -*-
import re
from collections import Counter

import jieba







# 定义分词函数
def cut_and_remove_stopwords(text):
    # 读取停用词文件
    text = re.sub(r"[^\w\s]", "", text)
    # with open("data/stop.txt", "r", encoding="gbk") as file:
    #     stopwords = [line.strip() for line in file.readlines()]
    stopwords = []
    words = jieba.cut(text)
    # 去除停用词
    stopwords = []
    words = [word for word in words if word not in stopwords]
    word_count = Counter(words)
    # 打印词频统计结果
    # for word, count in word_count.items():
    #     print(f"{word}: {count}")
    return word_count.items()


