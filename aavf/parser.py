from aavf.model import Header, Record

def parsekv(s):
    # internal function for parsing key-value pairs
    s = s.split('<')[1].split('>')[0]
    return {kv[0]: kv[1] for kv in map(lambda x: x.split('='), s.split(','))}

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
                # parse key-value pairs from ref line
                ref = parsekv(l)
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
    def __init__(self, fd, header=Header()):
        self.fd = fd
        print(header, file=self.fd)

    def writerecord(self, row):
        print(row, file=self.fd)
