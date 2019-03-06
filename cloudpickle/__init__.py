from __future__ import absolute_import

import sys


if sys.version_info[:2] >= (3, 8):
    from cloudpickle.cloudpickle_fast import *
else:
    from cloudpickle.cloudpickle import *

__version__ = '1.0.0'
