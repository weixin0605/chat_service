"""
分词
"""
import jieba
import config

jieba.load_userdict(config.user_dict_path)

def cut(senetence,by_word=False,use_stopwords=False,with_sg=False):
    """
    :param senetence: str句子
    :param by_word: 是否按照单个字
    :param use_stopwords:
    :param with_sg:
    :return:
    """

    pass