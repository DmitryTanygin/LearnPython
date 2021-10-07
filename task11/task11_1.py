def parse_cdp_neighbors(command_output):
    result = {}
    for line in command_output.split('\n'):
        line = line.split()
        if line == '':
            continue
        elif 'neighbors' in line:
            device = line[0].split('>')[0]
        elif 'Eth' in line:
            device_id = line[0]
            local_intrface = line[1] + line[2]
            port_id = ''.join(line[len(line) - 2: len(line)])
            result_key = (device, local_intrface)
            result_value = (device_id, port_id)
            result[result_key] = result_value
    return result


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
