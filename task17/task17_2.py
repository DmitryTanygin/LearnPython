import csv
import glob
import re

sh_version_files = glob.glob("sh_vers*")
# print(sh_version_files)
headers = ["hostname", "ios", "image", "uptime"]


def parse_sh_version(sh_version):
    match = re.search(r'Version (?P<ios>\S[^\,]+).'
                      r'+uptime is (?P<uptime>\S+\s\S+\s\S+\s\S+\s\S+\s\S+).'
                      r'+file is \"(?P<image>\S[^\"]+)', sh_version)
    return match.group('ios', 'image', 'uptime')


def write_inventory_to_csv(data_filenames, csv_filename):
    result = [headers]
    for filename in data_filenames:
        with open(filename) as f, open(csv_filename, 'w') as g:
            writer = csv.writer(g, quoting=csv.QUOTE_NONNUMERIC)
            hostname = re.search(r'.+\_+.+\_+(.+)\.txt', filename).group(1)
            list_parse = list(parse_sh_version(re.sub(r'\n', ' ', f.read())))
            list_parse.insert(0, hostname)
            result.append(list_parse)
            for line in result:
                writer.writerow(line)


write_inventory_to_csv(sh_version_files, 'routers_inventory.csv')
