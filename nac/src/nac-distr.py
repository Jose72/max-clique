#!/usr/bin/env python3

import os
import networkx as NX
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from algorithms.parallel import main


def run(graph, workers):
    G = NX.read_edgelist(graph)

    res = main(G, workers)

    print("Result: {}, size: {}".format(res, len(res)))


if __name__ == "__main__":
    parser = ArgumentParser(
        description='MCP',
        formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '--workers',
        default=os.cpu_count(),
        type=int,
        help='MCP workers'
    )

    parser.add_argument(
        '--graph',
        default=None,
        help='MCP graph data'
    )

    args = parser.parse_args()

    run(args.graph, args.workers)