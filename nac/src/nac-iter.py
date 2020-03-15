#!/usr/bin/env python3

import sys
import time
import networkx as NX

from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from algorithms.iterative import main

def test_graph(G):
    start = time.time()
    res = main(G)
    end = time.time()

    print("Result: {}, size: {}".format(res, len(res)))

    delta_own = end - start

    start = time.time()
    nx_clique = NX.graph_clique_number(G)
    end = time.time()

    print("Size NX: {}".format(nx_clique))

    delta_nx = end - start

    print("Time - Own: {}, NX: {}".format(delta_own, delta_nx))


def run():
    # Runs a Complete Graph
    # test
    if len(sys.argv) <= 1:
        g = NX.complete_graph(10)
        test_graph(g)
        return

    # Load a graph
    g = NX.read_edgelist(sys.argv[1])
    test_graph(g)


if __name__ == "__main__":
    run()

