
"""
获取停用词
"""
import config

stopwords = [i.strip() for i in open(config.stopwords_path, encoding='UTF-8').readlines()]
