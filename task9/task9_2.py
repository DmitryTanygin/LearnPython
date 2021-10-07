trunk_mode_template = ["switchport mode trunk",
                       "switchport trunk native vlan 999",
                       "switchport trunk allowed vlan"
                       ]
trunk_config = {"FastEthernet0/1": [10, 20, 30],
                "FastEthernet0/2": [11, 30],
                "FastEthernet0/4": [17]
                }


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result = []
    for interface, vlan in intf_vlan_mapping.items():
        result.append(f'interface {interface}')
        vlan = [str(i) for i in vlan]
        str_vlan = ','.join(vlan)
        for item in trunk_template:
            if item.endswith('allowed vlan'):
                result.append(f'{item} {str_vlan}')
            else:
                result.append(f'{item}')
    return result


for i in generate_trunk_config(trunk_config, trunk_mode_template):
    print(i)
