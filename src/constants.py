import pathlib

MAIN_DOC_URL = 'https://docs.python.org/3/'

MAIN_PEP_URL = 'https://peps.python.org/'

BASE_DIR = pathlib.Path(__file__).parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

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
