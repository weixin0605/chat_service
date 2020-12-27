"""
测试分类相关api
"""
from classify.build_model import build_classify_model,get_classify_model

if __name__=='__main__':
    # build_classify_model()
    model = get_classify_model()
    text = [
        "你 吃饭 了 吗",
        "今天 天气 很 好",
        "python",
        "python 好 学 吗"
    ]

    ret = model.predict(text)
    print(ret)