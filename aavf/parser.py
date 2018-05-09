from datetime import date
import pathlib
import hashlib
from aavf.model import Header, Record

class Reader(object):
    def __init__(self, path):
        self.reader = open(path)
        self._parse_header()
        self.records = map(self.parse_record, self.reader)
   
    def _parse_header(self):
        fileDate = None
        ref = None
        info = []
        line = next(self.reader)
        while line.startswith('##'):
            l = line.strip()[2:]
            ## process header lines
            if l.startswith('INFO'):
                pass
                # TODO: implement <key=value,..> parser 
                ##info.append(l.split('=')[1])
            elif l.startswith('reference'):
                ref = l.split('=')[1]
            elif l.startswith('fileDate'):
                fileDate = l.split('=')[1]

            line = next(self.reader)

        self.header = Header(fileDate=fileDate, reference=ref, info=info)

    @staticmethod
    def parse_record(line):
        r = line.split() 
        return Record(*r) # splat the line, validate input in Record.__init__

    def __iter__(self):
        return self.records 


class Writer(object):
    def __init__(self, fd, ref=None, fileDate=None):

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
        self.fd = fd
        print(Header(reference=self.reference, fileDate=fileDate), file=self.fd)


    def writerecord(self, row):
        print(Record(*row), file=self.fd)
