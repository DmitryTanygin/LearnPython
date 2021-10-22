import re
from pprint import pprint

with open('sh_cdp_n_sw1.txt') as f:
    str_result = re.sub(r'\n', ' ', f.read())


def parse_sh_cdp_neighbors(show_cdp_neighbors):
    hostname = re.search(r'(\S[^\>]+)', show_cdp_neighbors).group()
    list_result = re.findall(r'(\w+)\s+(\D+\d/\d)\s+\d+\D+\d+\s+(\D+\d/\d)', show_cdp_neighbors)
    result_dict_1 = {}
    result_dict_2 = {}
    for result in list_result:
        result_dict_1.update({result[1]: {result[0]: result[2]}})
    result_dict_2[hostname] = result_dict_1
    pprint(result_dict_2)


parse_sh_cdp_neighbors(str_result)
