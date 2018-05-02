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
    def __init__(self, CHROM, GENE, POS, REF, ALT):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass


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
