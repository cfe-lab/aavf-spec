from aavf import Reader


a = Reader("example.aavf")
print(a.header)
print(a.header.info)
for r in a:
    print(r)

