trunk_mode_template = ["switchport mode trunk",
                       "switchport trunk native vlan 999",
                       "switchport trunk allowed vlan"
                       ]
trunk_config = {"FastEthernet0/1": [10, 20, 30],
                "FastEthernet0/2": [11, 30],
                "FastEthernet0/4": [17]
                }


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    dict_result = {}
    for interface, vlan in intf_vlan_mapping.items():
        vlan = [str(i) for i in vlan]
        str_vlan = ','.join(vlan)
        result = []
        for item in trunk_template:
            if item.endswith('allowed vlan'):
                result.append(f'{item} {str_vlan}')
            else:
                result.append(f'{item}')
        dict_result[interface] = result

    return dict_result


config = generate_trunk_config(trunk_config, trunk_mode_template)

for key in config:
    print('' + '-' * 30)
    print(f'{key}:')
    for item in config[key]:
        print(f'{item}')

