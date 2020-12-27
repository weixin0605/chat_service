from prepar_corpus.prepar_user_dict.test_user_dict import test_user_dict
from lib.cut_sentence import cut
from lib import stopwords

if __name__ == '__main__':
    a = 'python和c++哪个难,UI/UE把,罢了被本'
    print(cut(a,with_sg=False,use_stopwords=True))
    # print(stopwords)

