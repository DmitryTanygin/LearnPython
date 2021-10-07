def convert_ranges_to_ip_list(ip_address):
    result = []
    for ip in ip_address:
        ip_list = ip.split('-')
        if len(ip_list) > 1:
            start_ip = ip_list[0]
            end_ip = ip_list[1]
            if not len(end_ip.split('.')) > 1:
                for i in range(int(start_ip.split('.')[3]), int(end_ip) + 1):
                    result.append(f"{'.'.join(start_ip.split('.')[0:3])}.{i}")
                    # print(f"{'.'.join(start_ip.split('.')[0:3])}.{i}")
            else:
                for i in range(int(start_ip.split('.')[3]), int(end_ip.split('.')[3]) + 1):
                    result.append(f"{'.'.join(start_ip.split('.')[0:3])}.{i}")
                    # print(f"{'.'.join(start_ip.split('.')[0:3])}.{i}")
        else:
            result.append(ip)
    return result


if __name__ == '__main__':
    print(convert_ranges_to_ip_list('8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132'))
