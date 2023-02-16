import pathlib

MAIN_DOC_URL = 'https://docs.python.org/3/'
MAIN_PEP_URL = 'https://peps.python.org/'

BASE_DIR = pathlib.Path(__file__).parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
PRETTY = 'pretty'
FILE = 'file'
DEFAULT = 'default'
LOG_DIR = BASE_DIR / 'logs'
PARSER_LOG = 'parser.log'
DOWNLOADS = 'downloads'
RESULTS = 'results'
ALL_VERSIONS = 'All versions'

EXPECTED_STATUSES = (
    'Active',
    'Accepted',
    'Deferred',
    'Final'
    'Provisional',
    'Rejected',
    'Superseded',
    'Withdrawn',
    'Draft',
    'Active',
)


# я решал без этих констант,
# но их пришлось вставить, чтобы пройти pytest
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
