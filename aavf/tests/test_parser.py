from aavf import Reader, Writer

import unittest

reader = Reader("example.aavf")

old_records = []
with open("/tmp/test.aavf", 'wb') as fd:
    w = Writer(fd, header=reader.header)
    for r in reader:
        old_records.append(r)
        w.writerecord(r)

for r1, r2 in zip(Reader("/tmp/test.aavf"), old_records):
    print(r1,r2)



