import unittest
import networkx as NX

import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from TTT import maxclique

TXT = 'txt'
CLQ = 'clq'

workers_num = 10

PATH = '../../graphs/{}.{}'

def calc_and_compare(name, extension):

    path_name = PATH.format(name, extension)

    result = len(main(path_name, workers_num))
    
    nx_result = NX.graph_clique_number(create_graph_from_file(path_name))
    
    return result == nx_result

def create_graph_from_file(graph_name):
    return NX.read_edgelist(graph_name)

class ResultTests(unittest.TestCase):
    def test_result_brock_200_2(self):
        assert(calc_and_compare('brock200_2', TXT))
    def test_result_brock_200_4(self):
        assert(calc_and_compare('brock200_4', TXT))
    def test_result_brock_400_2(self):
        assert(calc_and_compare('brock400_2', TXT))
    def test_result_brock_400_4(self):
        assert(calc_and_compare('brock400_4', TXT))
    def test_result_brock_800_2(self):
        assert(calc_and_compare('brock800_2', TXT))
    def test_result_brock_800_4(self):
        assert(calc_and_compare('brock800_4', TXT))
    def test_result_keller5(self):
        assert(calc_and_compare('keller5', TXT))
    def test_result_c125_9(self):
        assert(calc_and_compare('c125.9', CLQ))
    def test_result_c250_9(self):
        assert(calc_and_compare('c250.9', CLQ))
    def test_small_graph(self):
        assert(calc_and_compare('small-graph', CLQ))

if __name__ == "__main__":
    unittest.main()

