# Utility functions
# Author: Tim Fleming, Mar 2022

from operator import truediv
import os
import time
import logging
import datetime
import random

logger = logging.getLogger(__name__)

def get_base_filename(pathname):
    """
    Get the name of a file, sans extension, from a full path name.
    """
    base = os.path.basename(pathname)
    return os.path.splitext(base)[0]


def safe_mkdir(path):
    """
    Make a directory if it doesn't exist.
    """
    if not os.path.exists(path):
        logger.info('creating output directory "{}'.format(path))
        os.makedirs(path)

# given a weight value between 0-1, returns true if a randon number is less that it is
def made_weight(wgt):
    if wgt is None:
        return True

    return random.random() < wgt

def format_date(dt):
    # YYYY-MM-DD
    return dt.strftime('%Y-%m-%d')

def to_iso(dt):
    # iso string
    return dt.isoformat()