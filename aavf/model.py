from os import path, access, R_OK
from datetime import date
import pathlib
import hashlib
import sys

def sha256(fd):
    pass

class Header(object):
    """AAVF Header
    """
    def __init__(self, ref, fileformat='AAVFv1.0', fileDate=None):
        # I'm enforcing that Headers are initialized with a refernce
        # sequence right now
        if not (path.isfile(ref) and access(ref, R_OK)):
            raise Exception
        self.reference = {'URI': pathlib.Path(ref).as_uri(),
                          'SHA256': sha256(open(ref, 'rb')),
                          'ACCESSION': None}
        if fileDate is None:
            fileDate = date.today().isoformat().replace('-', '')
        self.fileDate = fileDate

        self.info = []
        self.filters = []

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
        # it is not sufficient that the genes are the same if we're
        # comparing positions from different reference coordinates
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
