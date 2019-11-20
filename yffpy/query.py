__author__ = "Wren J. R. (uberfastman)"
__email__ = "wrenjr@yahoo.com"

import warnings

warnings.warn(
    "yffpy has been DEPRECATED and replaced by yfpy: https://pypi.org/project/yfpy/\n"
    "Please upgrade your project dependencies.",
    DeprecationWarning
)

from yfpy.query import *
