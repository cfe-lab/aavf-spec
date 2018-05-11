from datetime import date
import pathlib
import hashlib

class Header(object):
    """AAVF Header
    """
    def __init__(self, reference=None, source='AAVFv0.1', fileDate=None,
            info={}):
        if reference is not None:
            self.reference = reference 
#            if 'URI' in reference:
#                ref = pathlib.Path(reference['URI'])
#                if not ref.exists():
                    # raise a warning that the reference URI doesn't exist?
#                    pass

#                self.reference = {'URI': pathlib.Path(ref).as_uri(),
#                                  'SHA256': sha256(open(ref, 'rb')),
#                                  'ACCESSION': None}
        else:
            self.reference = None
        
        if fileDate is None:
            fileDate = date.today().isoformat().replace('-', '')
        self.fileDate = fileDate

        self.source = source
        self.info = info
        self.filters = []

    def __repr__(self):
        return "Header(ref={}, fileDate={})".format(self.reference,
                self.fileDate)

    def __str__(self):
        s = []
        if self.reference:
            s.append("##reference=<" + ','.join(["{}={}".format(k,
                self.reference[k]) for k in self.reference.keys()]) + '>')
        s.append("##fileDate=" + self.fileDate)
        s.append("##source=" + self.source)

        # always last:
        s.append('\t'.join(["#CHROM", "GENE", "POS", "REF", "ALT", "FILTER",
        "ALT_FREQ", "COVERAGE INFO"]))
        return '\n'.join(s)


class Record(object):
    """AAVF Record
    """
    def __init__(self, CHROM, GENE, POS, REF, ALT, FILTER, ALT_FREQ,
                 COVERAGE, INFO='.'):
        self.CHROM = CHROM
        self.GENE = GENE
        self.POS = POS
        self.REF = REF
        self.ALT = ALT
        self.FILTER = FILTER
        self.ALT_FREQ = ALT_FREQ
        self.COVERAGE = COVERAGE
        self.INFO = INFO

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        # it would be better if we also check that the reference
        # coordinate system was the same
        return self.GENE == other.GENE and self.POS < other.POS 

    def __repr__(self):
        return "Record(CHROM=%(CHROM)s, GENE=%(GENE)s, POS=%(POS)s, REF=%(REF)s, ALT=%(ALT)s)" % self.__dict__

    def __str__(self):
        return "\t".join([self.CHROM, self.GENE, self.POS, self.REF, self.ALT,
            self.FILTER, self.ALT_FREQ, self.COVERAGE, self.INFO])

class AAVF(object):
    """AAVF Files have a header and a list of records
    """
    def __init__(self, header, records):
        self.header = header
        self.records = records

    def __iter__(self):
        return iter(self.records)

    def validate(self):
        pass
