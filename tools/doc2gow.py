import networkx as nx
from tools.preprocess import Token

# converts a document to a k-core graph specified by
# Rousseau F., Vazirgiannis M. (2015) Main Core Retention on
# Graph-of-Words for Single-Document Keyword Extraction.
# In: Hanbury A., Kazai G., Rauber A., Fuhr N. (eds)
# Advances in Information Retrieval. ECIR 2015.
# Lecture Notes in Computer Science, vol 9022. Springer, Cham

class DocToGow(object):
    # document to Graph-of-Words

    def __init__(self, document : list):
        # document : list of Token
        self.document = document

    def get_gow(self, method, is_stop_word=lambda w : False, filter=lambda w : True, **kwargs):
        # method \in "nd" for unweighted non-directed, "wnd" for weighted non-directed,
        #  "fd" for forward-directed, "bd" for backward-directed
        if method in ["nd", "wnd"]:
            return self._get_non_directed_gow(method, is_stop_word, filter, **kwargs)
        else:
            raise Exception("Method %s not implemented" % method)

    def _get_non_directed_gow(self, method, is_stop_word, filter, window_size=5):
        g = nx.Graph()
        for idx, center in enumerate(self.document):
            # For each token, visit its neighbors
            if is_stop_word(center) or not filter(center):
                continue
            for neighbor in self.document[
                            idx + 1:
                            min(idx + window_size, len(self.document))]:
                if is_stop_word(neighbor) or not filter(center):
                    continue
                if not g.has_edge(center, neighbor):
                    g.add_edge(center, neighbor)
                    if method == "wnd":
                        g[center][neighbor]['weight'] = 1
                elif method == "wnd":
                    g[center][neighbor]['weight'] += 1
        return g






