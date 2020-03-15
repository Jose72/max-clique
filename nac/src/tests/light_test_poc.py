import unittest
import networkx as NX

import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from TTT_iter import max_clique

def calc_and_compare(G):
    result = len(max_clique(G))
    nx_result = NX.graph_clique_number(G)
    return result == nx_result

class ResultTests(unittest.TestCase):

    def test_result_cycle_graph_20(self):
        assert(calc_and_compare(NX.cycle_graph(20)))
    def test_result_cycle_graph_200(self):
        assert(calc_and_compare(NX.cycle_graph(200)))
    def test_result_cycle_graph_10(self):
        assert(calc_and_compare(NX.cycle_graph(10)))
    def test_result_cycle_graph_2(self):
        assert(calc_and_compare(NX.cycle_graph(2)))
    def test_result_cycle_graph_3(self):
        assert(calc_and_compare(NX.cycle_graph(3)))
    def test_result_complete_graph_2(self):
        assert(calc_and_compare(NX.complete_graph(2)))
    def test_result_complete_graph_200(self):
        assert(calc_and_compare(NX.complete_graph(200)))
    def test_result_balanced_binary_tree_height_10(self):
        assert(calc_and_compare(NX.balanced_tree(2, 10)))
    def test_result_balanced_triary_tree_height_8(self):
        assert(calc_and_compare(NX.balanced_tree(3, 8)))
    def test_result_balanced_4ary_tree_height_5(self):
        assert(calc_and_compare(NX.balanced_tree(4, 5)))
    def test_result_balanced_5ary_tree_height_10(self):
        assert(calc_and_compare(NX.balanced_tree(5, 4)))
    def test_result_balanced_binary_tree_height_15(self):
        assert(calc_and_compare(NX.balanced_tree(2, 15)))
    def test_result_barbell_graph_10_2(self):
        assert(calc_and_compare(NX.barbell_graph(10, 2)))
    def test_result_barbell_graph_5_5(self):
        assert(calc_and_compare(NX.barbell_graph(5, 5)))
    def test_result_barbell_graph_20_10(self):
        assert(calc_and_compare(NX.barbell_graph(20, 10)))
    def test_result_circular_ladder_graph_20(self):
        assert(calc_and_compare(NX.circular_ladder_graph(20)))
    def test_result_circular_ladder_graph_10(self):
        assert(calc_and_compare(NX.circular_ladder_graph(10)))
    def test_result_circular_ladder_graph_5(self):
        assert(calc_and_compare(NX.circular_ladder_graph(5)))
    def test_result_gnp_50_0_5_1(self):
        assert(calc_and_compare(NX.gnp_random_graph(50, 0.5, 1)))
    def test_result_gnp_50_0_5_2(self):
        assert(calc_and_compare(NX.gnp_random_graph(50, 0.5, 2)))
    def test_result_gnp_50_0_5_3(self):
        assert(calc_and_compare(NX.gnp_random_graph(50, 0.5, 3)))
    def test_result_gnp_50_0_5_4(self):
        assert(calc_and_compare(NX.gnp_random_graph(50, 0.5, 4)))
    def test_result_gnp_50_0_5_5(self):
        assert(calc_and_compare(NX.gnp_random_graph(50, 0.5, 5)))
    def test_result_gnp_50_0_5_6(self):
        assert(calc_and_compare(NX.gnp_random_graph(50, 0.5, 6)))
    def test_result_gnp_50_0_5_7(self):
        assert(calc_and_compare(NX.gnp_random_graph(50, 0.5, 7)))
    def test_result_gnp_50_0_95_1(self):
        assert(calc_and_compare(NX.gnp_random_graph(20, 0.95, 8)))
    def test_result_gnp_50_0_95_2(self):
        assert(calc_and_compare(NX.gnp_random_graph(20, 0.95, 9)))
    def test_result_gnp_50_0_95_3(self):
        assert(calc_and_compare(NX.gnp_random_graph(20, 0.95, 10)))
    def test_result_gnp_50_0_95_4(self):
        assert(calc_and_compare(NX.gnp_random_graph(20, 0.95, 11)))
    def test_result_empty_graph(self):
        assert(calc_and_compare(NX.empty_graph()))
    def test_result_full_5ary_tree_4_tall(self):
        assert(calc_and_compare(NX.full_rary_tree(5, 4)))
    def test_result_ladder_graph_200(self):
        assert(calc_and_compare(NX.ladder_graph(200)))
    def test_result_lollipop_graph_200_20(self):
        assert(calc_and_compare(NX.lollipop_graph(200, 20)))
    def test_result_null_graph(self):
        assert(calc_and_compare(NX.null_graph()))
    def test_result_path_graph_200(self):
        assert(calc_and_compare(NX.path_graph(200)))
    def test_result_star_graph_50(self):
        assert(calc_and_compare(NX.star_graph(50)))
    def test_result_trivial_graph(self):
        assert(calc_and_compare(NX.trivial_graph()))
    def test_result_turan_graph_50_20(self):
        assert(calc_and_compare(NX.turan_graph(50, 5)))
    def test_result_wheel_graph(self):
        assert(calc_and_compare(NX.wheel_graph(50)))

if __name__ == "__main__":
    unittest.main()
