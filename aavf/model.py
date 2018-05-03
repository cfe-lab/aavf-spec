class Header(object):
    """AAVF Header
    """
    def __init__(self, reference=None, source='AAVFv0.1', fileDate=None, info=[]):
        self.reference = reference
        self.source = source
        self.fileDate = fileDate
        self.info = info

    def __str__(self):
        return "Header(ref=\"{}\", fileDate=\"{}\")".format(self.reference,
                self.fileDate)

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

    def __str__(self):
        return "Record(CHROM=%(CHROM)s, GENE=%(GENE)s, POS=%(POS)s, REF=%(REF)s, ALT=%(ALT)s)" % self.__dict__


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
