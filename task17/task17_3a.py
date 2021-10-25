import re
import yaml
from pprint import pprint


def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    result = {}
    for file in list_of_files:
        result_dict_1 = {}
        with open(file) as f:
            str_result = re.sub(r'\n', ' ', f.read())
            hostname = re.search(r'(\S[^\>]+)', str_result).group()
            list_result = re.findall(r'(\w+)\s+(\D+\d/\d)\s+\d+\s+\D?\s?\D\s\D\s+\S+\s+(\D+\d/\d)', str_result)

            for result_dict_2 in list_result:
                result_dict_1.update({result_dict_2[1]: {result_dict_2[0]: result_dict_2[2]}})
            result[hostname] = result_dict_1
    pprint(result)
    with open(save_to_filename, 'w') as g:
        yaml.dump(result, g)


generate_topology_from_cdp(['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt',
                            'sh_cdp_n_r4.txt', 'sh_cdp_n_r5.txt', 'sh_cdp_n_r6.txt'], 'topology.yaml')
