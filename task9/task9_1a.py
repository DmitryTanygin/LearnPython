access_mode_template = ["switchport mode access",
                        "switchport access vlan",
                        "switchport nonegotiate",
                        "spanning-tree portfast",
                        "spanning-tree bpduguard enable"
                        ]
port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]
access_config = {"FastEthernet0/12": 10,
                 "FastEthernet0/14": 11,
                 "FastEthernet0/16": 17
                 }
access_config_2 = {"FastEthernet0/03": 100,
                   "FastEthernet0/07": 101,
                   "FastEthernet0/09": 107,
                   }


def generate_access_config(intf_vlan_mapping, access_template, port_security=None):
    result = []
    for interface, vlan in intf_vlan_mapping.items():
        result.append(f'interface {interface}')
        for item in access_template:
            if item.endswith('access vlan'):
                result.append(f'{item} {vlan}')
            else:
                result.append(f'{item}')
        if port_security is not None:
            for port in port_security:
                result.append(port)
    return result


a = generate_access_config(access_config, access_mode_template, port_security_template)
# b = generate_access_config(access_config_2, access_mode_template)
for t in a:
    print(t)
# for t in b:
#     print(t)
