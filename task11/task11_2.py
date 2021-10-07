from task11_1 import parse_cdp_neighbors
from pprint import pprint

infiles = ["sh_cdp_n_sw1.txt", "sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt", "sh_cdp_n_r3.txt"]


def create_network_map(filenames):
    topology = {}
    for file in filenames:
        with open(file) as f:
            topology.update(parse_cdp_neighbors(f.read()))
    return unique_network_map(topology)


def unique_network_map(topology_dict):
    topology = {}
    for key, value in topology_dict.items():
        if not key in topology.values():
            topology[key] = value
    return topology


if __name__ == "__main__":
    pprint(unique_network_map(create_network_map(infiles)), depth=2)
    # print(unique_network_map(create_network_map(infiles)))
