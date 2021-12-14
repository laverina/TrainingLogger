import sys
from _pytest.assertion import truncate
sys.path.append('../')


truncate.DEFAULT_MAX_CHARS = 1000
truncate.DEFAULT_MAX_LINES = 1000
