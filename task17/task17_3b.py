from pprint import pprint
from LearnPython.task11.task11_2a import draw_topology
from LearnPython.task11.task11_2 import unique_network_map

import yaml


def transform_topology(filename):
    with open(filename) as f:
        template_dict = yaml.safe_load(f)
        result = {}
        for keys, values in template_dict.items():
            for keys2, values2 in values.items():
                result_key = keys, keys2
                result_value = [(key, values2[key]) for key in values2.keys()][0]
                result[result_key] = result_value
        draw_topology(unique_network_map(result))


transform_topology('topology.yaml')
