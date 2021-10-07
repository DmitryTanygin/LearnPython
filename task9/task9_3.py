def get_int_vlan_map(config_filename):
    result = {}
    with open(config_filename) as f:
        for line in f:
            if 'interface FastEthernet' in line:
                interface = line.split()[1]
            elif 'access vlan' in line:
                vlan = int(line.split()[3])
                result[interface] = vlan
            elif 'allowed vlan' in line:
                vlan = line.split()[4].split(',')
                # int_list_vlan = [int(i) for i in vlan.split(',')]
                result[interface] = [int(i) for i in vlan]
        print(result)


get_int_vlan_map('config_sw1.txt')
