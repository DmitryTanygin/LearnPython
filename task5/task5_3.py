interface = input('Введите режим работы интерфейса (access/trunk): ')
interface_type = input('Введите тип и номер интерфейса: ')
vlan = input('Введите номер влан(ов): ')

template = {'access': ["switchport mode access", "switchport access vlan {}",
                       "switchport nonegotiate", "spanning-tree portfast",
                       "spanning-tree bpduguard enable"
                       ],
            'trunk': ["switchport trunk encapsulation dot1q", "switchport mode trunk",
                      "switchport trunk allowed vlan {}"
                      ]
            }

print('\n' + '-' * 30)
print(f'interface {interface_type}')
print('\n'.join(template[interface]).format(vlan))
