mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
for macs in mac:
    result.append('.'.join(macs.split(':')))

print(result)
