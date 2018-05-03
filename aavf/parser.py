from datetime import date
import pathlib
import hashlib
from aavf.model import Header, Record

class Reader(object):
    def __init__(self, path):
        self.header, rest = parse_header(fd)
        self.records = map(parse_record, rest)
    
    def parse_header(self, fd):
        fileDate = None
        ref = None
        info = []
        for line in fd.readline():
            if line.split()[0] != '#CHROM':
                return fd

        return Header(fileDate=fileDate, ref=ref, info=info)

    def parse_record(self, line):
        r = line.strip().split() 
        return Record(r[0], r[1], r[2], r[3], r[4], r[5], r[6])

    def __iter__(self):
        return self.records


class Writer(object):
    def __init__(self, ref=None, fileDate=None):

        if ref is not None:
            ref = pathlib.Path(ref)
            if not ref.exists():
                raise Exception
            self.reference = {'URI': pathlib.Path(ref).as_uri(),
                              'SHA256': sha256(open(ref, 'rb')),
                              'ACCESSION': None}
        
        if fileDate is None:
            fileDate = date.today().isoformat().replace('-', '')
        self.fileDate = fileDate

        self.info = []
        self.filters = []

