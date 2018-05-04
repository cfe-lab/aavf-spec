from aavf import Reader

import unittest

a = Reader("example.aavf")
print(a.header)
for r in a:
    print(r)

