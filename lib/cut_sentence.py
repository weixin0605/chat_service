"""
分词
"""
import jieba
import jieba.posseg as psg
import config
import string
from lib import stopwords
import logging


# 关闭jieba log
jieba.setLogLevel(logging.INFO)
jieba.load_userdict(config.user_dict_path)


# 所有小写字母
# string.ascii_lowercase
# 准备英文词典
letters = string.ascii_lowercase+'+'+'/'

def cut_sentence_by_word(sentence):
    """
    实现中英文分词
    :param sentence:str句子
    :return:
    """
    result = []
    temp = ""
    for word in sentence:
        if word.lower() in letters:
            temp+=word
        else:
            if temp != '':
                result.append(temp.lower())
                temp = ""
            result.append(word.strip())
    if temp != "":
        result.append(temp.lower())
        temp = ""
    return result

def cut(senetence,by_word=False,use_stopwords=False,with_sg=False):
    """
    :param senetence: str句子
    :param by_word: 是否按照单个字
    :param use_stopwords:是否使用停用词
    :param with_sg:是否返回词性
    :return:
    """
    if by_word:
        result = cut_sentence_by_word(senetence)
    else:
        result = psg.lcut(senetence)
        result = [(i.word,i.flag) for i in result]
        if not with_sg:
            result = [i[0] for i in result]
            # 是否使用停用词
            if use_stopwords:
                result = [i for i in result if i not in stopwords]
        else:
            result = [i for i in result if i[0] not in stopwords]

    return result

if __name__=='__main__':
    a = 'python和c++哪个难,UI/UE'
    print(cut_sentence_by_word(a))