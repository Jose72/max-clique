import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from algorithms.neighbors import Neighbors

CLIQUE = set()


def generate_degree_list(G, cand):
    degree_list = []
    for v in cand:
        degree_list.append((G.degree(v), v))
    degree_list.sort(key=lambda x: (x[0], x[1]))
    return degree_list


def compute_neigh(G, k_size, cand, degree_list):
    neighs = Neighbors()
    prev_degree_counted = {}

    local_degree_list = [v for v in degree_list if v[1] in cand]

    first_degree = local_degree_list[0][0]
    previous_n = k_size

    for d in local_degree_list:
        magic_number = k_size + 1 + prev_degree_counted.get(d[0] - 1, 0)
        k_wanted = d[0] + 1
        aux_degree = d[0]
        found = magic_number >= k_wanted
        fall_back = k_wanted < first_degree + 1

        while (not fall_back) and (not found) and (k_wanted > previous_n) and (aux_degree > 0):
            k_wanted -= 1
            aux_degree -= 1
            magic_number += prev_degree_counted.get(aux_degree, 0)
            found = magic_number >= k_wanted
            fall_back = k_wanted < first_degree + 1

        n_number = previous_n
        if found:
            n_number = k_wanted
        else:
            if fall_back:
                n_number = previous_n + 1

        neighs.add(n_number, d[1])

        previous_n = n_number
        prev_degree_counted[d[0]] = 1 + prev_degree_counted.get(d[0], 0)

    return neighs


def explore(v, G, K, cand, deep, degree_list, fini):
    global CLIQUE

    Kq = K | {v}

    candl = (set(G.neighbors(v)) & cand) - fini

    if len(candl) > 0:

        neighs = compute_neigh(G, len(Kq), candl, degree_list)

        k_neigh, next_neigh = neighs.get_n_n()

        while (next_neigh is not None) and (k_neigh > max(len(CLIQUE), len(Kq))):
            explore(next_neigh, G, Kq, (candl & set(G.neighbors(next_neigh))), deep + 1, degree_list, fini)

            k_neigh, next_neigh = neighs.get_n_n()

            candl = candl - {next_neigh}

    if len(Kq) > len(CLIQUE):
        CLIQUE = Kq.copy()



def main(G):
    nodes = G.nodes()

    # print("max-clique - nodes: {}".format(nodes))

    # Order nodes by its degree
    nodes = list(map(lambda x: (x, G.degree(x)), nodes))
    nodes = sorted(nodes, key=lambda x: x[1])
    nodes = list(map(lambda x: x[0], nodes))

    degree_list = generate_degree_list(G, set(nodes))

    fini = set()

    for v in nodes:

        if G.degree(v) >= len(CLIQUE):

            cand = set(G.neighbors(v))

            explore(v, G, set(), cand, 1, degree_list, fini)

            fini = fini | {v}

    return list(CLIQUE)
