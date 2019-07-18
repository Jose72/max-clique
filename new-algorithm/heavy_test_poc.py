import unittest
import networkx as NX
from poc import main

def calc_and_compare(G):
    result = len(main(G))
    nx_result = NX.graph_clique_number(G)
    return result == nx_result

default_seed = 1

class ResultTests(unittest.TestCase):
    def test_result_gnp_50_0_99(self):
        assert(calc_and_compare(NX.gnp_random_graph(50, 0.99, default_seed)))
    def test_result_gnp_100_0_80(self):
        assert(calc_and_compare(NX.gnp_random_graph(100, 0.80, default_seed)))
    def test_result_circulant_graph_100(self):
        assert(calc_and_compare(NX.circulant_graph(100, [1,2,3])))
    def test_result_dgm_200(self):
        assert(calc_and_compare(NX.dorogovtsev_goltsev_mendes_graph(10)))
    


if __name__ == "__main__":
    unittest.main()