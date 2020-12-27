import pandas
from lib import cut
from tqdm import tqdm
import config
import json
import random

# 1/5数据测试集
flags = [0,0,0,0,1]

# 闲聊语料
xiaohuangji_path = r"corpus/orgin_corpus/小黄鸡未分词.conv"
# 问答语料
byhand_path = r"corpus/orgin_corpus/手动构造的问题.json"
crawled_path = r"corpus/orgin_corpus/爬虫抓取的问题.csv"

def keywoads_in_line(line):
    # 判断line中是否存在不符合要求的词
    keywords_list = ["传智播客",'xxx','黑马']
    for word in line:
        if word in keywords_list:
            return True
        else:
            return False

def process_xiaohuangji(f_train,f_test):
    """处理小黄鸡语料"""
    num_train = 0
    num_test = 0
    ret = open(xiaohuangji_path,encoding='UTF-8').readlines()
    flag = 0
    for line in tqdm(ret,desc='小黄鸡'):
        # 句子长度为1考虑删除
        if line.startswith("E"):
            flag = 0
            continue
        elif line.startswith("M"):
            if flag == 0:
                line = line[1:].strip()
                flag = 1
            else:
                continue
        line_cuted = cut(line)
        if not keywoads_in_line((line_cuted)):
            line_cuted = " ".join(line_cuted)+"\t"+"__label__chat"
            if random.choice(flags) == 0:
                num_train += 1
                f_train.write(line_cuted+"\n")
            else:
                num_test += 1
                f_test.write(line_cuted+"\n")
    return num_train,num_test

def process_byhand_data(f_train,f_test):
    """处理手工构造的数据"""
    num_train = 0
    num_test = 0
    total_lines = json.loads(open(byhand_path,encoding='UTF-8').read())
    for key in (total_lines):
        for lines in tqdm(total_lines[key],desc='byhand'):
            for line in lines:
                # 去除个别不要的问题
                if "校区" in line:
                    continue
                line_cuted = cut(line)
                line_cuted = " ".join(line_cuted) + "\t" + "__label__QA"

                if random.choice(flags) == 0:
                    num_train += 1
                    f_train.write(line_cuted + "\n")
                else:
                    num_test += 1
                    f_test.write(line_cuted + "\n")
    return num_train,num_test

def process_crawled_data(f_train,f_test):
    """处理爬取的数据"""
    num_train = 0
    num_test = 0
    for line in tqdm(open(crawled_path,encoding='UTF-8').readlines(),desc='crawled'):
        line_cuted = cut(line)
        line_cuted = " ".join(line_cuted).replace("\n", "") + "\t" + "__label__QA"
        if random.choice(flags) == 0:
            num_train += 1
            f_train.write(line_cuted + "\n")
        else:
            num_test += 1
            f_test.write(line_cuted + "\n")
    return num_train,num_test


def proecss():
    f_train = open(config.classify_corpus_train_path,'a',encoding='UTF-8')
    f_test = open(config.classify_corpus_test_path,'a',encoding='UTF-8')
    # 处理小黄鸡
    num_chat_train,num_chat_test = process_xiaohuangji(f_train,f_test)
    # 处理手动构造的句子
    num_qa_train,num_qa_test = process_byhand_data(f_train,f_test)
    # 处理抓取的句子
    _a,_b = process_crawled_data(f_train,f_test)
    num_qa_train +=_a
    num_qa_test +=_b
    f_train.close()
    f_test.close()
    print("训练集和测试集：",num_chat_train+num_qa_train,num_chat_test+num_qa_test)
    print("QA语料和chat语料：",num_chat_test+num_chat_train,num_qa_test+num_qa_train)
