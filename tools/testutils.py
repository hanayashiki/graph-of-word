from tools.caption_process import CaptionProcess
from tools.preprocess import Preprocess
from tools.doc2gow import DocToGow
from tools.stopwords import ListStopWords
import networkx as nx
import matplotlib.pyplot as plt

class TestEnv(object):

    def __init__(self, document, stop_words="../data/tools/百度停用词表.txt"):
        document = document.strip()
        self.stop_words = ListStopWords(stop_words)
        self.preprocess = Preprocess()
        self.token_list = self.preprocess.tokenize(document)
        self.doc_to_gow = DocToGow(self.token_list)

def display_graph(g : nx.Graph, title="untitled"):
    pos = nx.spring_layout(g, scale=2)

    nx.draw_networkx(g, pos, font_family="SimHei", font_color="blue")

    nx.draw_networkx_edge_labels(g, pos=pos,font_family="SimHei", font_color="red",
                                 edge_labels=nx.get_edge_attributes(g,'weight'))
    plt.title(title)
    plt.show()