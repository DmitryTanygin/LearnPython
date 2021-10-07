def get_int_vlan_map(config_filename):
    result = {}
    with open(config_filename) as f:
        for line in f:
            if 'interface FastEthernet' in line:
                interface = line.split()[1]
                result[interface] = 1
            elif 'access vlan' in line:
                int_list_vlan = int(line.split()[3])
                result[interface] = int_list_vlan
            elif 'allowed vlan' in line:
                vlan = line.split()[4]
                list_vlan = vlan.split(',')
                int_list_vlan = [int(i) for i in list_vlan]
                result[interface] = int_list_vlan

        print(result)


get_int_vlan_map('config_sw2.txt')
