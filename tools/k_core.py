import networkx as nx

def k_core_undirected_unweighted(g : nx.Graph):
    core_number = nx.core_number(g)
    k = max(core_number.values())
    return k, nx.k_core(g, core_number=core_number)