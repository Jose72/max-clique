import unittest
import networkx as NX

import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from TTT_iter import max_clique

TXT = 'txt'
CLQ = 'clq'

def calc_and_compare(G):
    result = len(max_clique(G))
    nx_result = NX.graph_clique_number(G)
    return result == nx_result

def create_graph_from_file(graph_name, extension):
    return NX.read_edgelist('../../graphs/{}.{}'.format(graph_name, extension))

class ResultTests(unittest.TestCase):
    def test_result_brock_200_2(self):
        assert(calc_and_compare(create_graph_from_file('brock200_2', TXT)))
    def test_result_brock_200_4(self):
        assert(calc_and_compare(create_graph_from_file('brock200_4', TXT)))
    def test_result_brock_400_2(self):
        assert(calc_and_compare(create_graph_from_file('brock400_2', TXT)))
    def test_result_brock_400_4(self):
        assert(calc_and_compare(create_graph_from_file('brock400_4', TXT)))
    def test_result_brock_800_2(self):
        assert(calc_and_compare(create_graph_from_file('brock800_2', TXT)))
    def test_result_brock_800_4(self):
        assert(calc_and_compare(create_graph_from_file('brock800_4', TXT)))
    def test_result_keller5(self):
        assert(calc_and_compare(create_graph_from_file('keller5', TXT)))
    def test_result_c125_9(self):
        assert(calc_and_compare(create_graph_from_file('c125.9', CLQ)))
    def test_result_c250_9(self):
        assert(calc_and_compare(create_graph_from_file('c250.9', CLQ)))
    def test_small_graph(self):
        assert(calc_and_compare(create_graph_from_file('small-graph', CLQ)))

if __name__ == "__main__":
    unittest.main()

