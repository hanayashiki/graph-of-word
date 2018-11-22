from tools.caption_process import CaptionProcess
from tools.preprocess import Preprocess
from tools.doc2gow import DocToGow
from tools.stopwords import ListStopWords
from tools.testutils import TestEnv, display_graph
from tools.k_core import *
import json
import networkx as nx

def TestCaptionProcess():
    cp = CaptionProcess('../data/captions/数据结构')
    result = cp.process(do_sort=True)
    print(json.dumps(result, ensure_ascii=False, indent=2))

    result = cp.process(do_sort=True,
                        join_subtitles=True)
    print(json.dumps(result, ensure_ascii=False, indent=2))


# TestCaptionProcess()

def TestPreprocess():
    prep = Preprocess()
    token_list = prep.tokenize(
    """
    考察这个由13个整数所构成的\n待排序序列
    采用希尔排序算法\n我们首先将矩阵的宽度取作8\n于是我们按照不超过8个元素为准则\n将整个序列分为两段\n而每一段都对应于矩阵的一行\n这样我们就得到了一个宽度为8的矩阵
    """.strip()
    )
    for token in token_list:
        print(vars(token))

# TestPreprocess()

def TestDoc2Gow():
    doc = \
    """
    考察这个由13个整数所构成的\n待排序序列
    采用希尔排序算法\n我们首先将矩阵的宽度取作8\n于是我们按照不超过8个元素为准则\n将整个序列分为两段\n而每一段都对应于矩阵的一行\n这样我们就得到了一个宽度为8的矩阵
    """
    env = TestEnv(doc)
    for token in env.token_list:
        print(vars(token), " stop word ? ", env.stop_words.get_judger()(token))

    dtg = env.doc_to_gow

    gow = dtg.get_gow(method="wnd",
                      is_stop_word=env.stop_words.get_judger(),
                      window_size=5)

    display_graph(gow)

# TestDoc2Gow()

def TestKCore():
    doc = \
    """
    考察这个由13个整数所构成的\n待排序序列
    采用希尔排序算法\n我们首先将矩阵的宽度取作8\n于是我们按照不超过8个元素为准则\n将整个序列分为两段\n而每一段都对应于矩阵的一行\n这样我们就得到了一个宽度为8的矩阵
    """
    env = TestEnv(doc)
    for token in env.token_list:
        print(vars(token), " stop word ? ", env.stop_words.get_judger()(token))

    dtg = env.doc_to_gow

    gow = dtg.get_gow(method="wnd",
                      is_stop_word=env.stop_words.get_judger(),
                      window_size=5)

    display_graph(gow)

    k, k_core = k_core_undirected_unweighted(gow)

    display_graph(k_core, "k=%d" % k)


TestKCore()