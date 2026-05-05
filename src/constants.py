from pathlib import Path

MAIN_DOC_URL = 'https://docs.python.org/3/'
PEP_DOC_URL = 'https://peps.python.org/'
BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

EXPECTED_STATUS = {
     'A': ('Active', 'Accepted'),
     'D': ('Deferred',),
     'F': ('Final',),
     'P': ('Provisional',),
     'R': ('Rejected',),
     'S': ('Superseded',),
     'W': ('Withdrawn',),
     '': ('Draft', 'Active'),
 }

MAX_STATUS_LENGTH = 20
MAX_COUNT_LENGTH = 10
TOTAL_WIDTH = 35

OUTPUT_PRETTY_TABLE = 'pretty'
OUTPUT_FILE = 'file'
LOGS_DIR = 'logs'
RESULTS_DIR = 'results'
DOWNLOADS_DIR = 'downloads'
