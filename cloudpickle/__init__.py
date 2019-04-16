from __future__ import absolute_import

import sys
import pickle


if hasattr(pickle.Pickler, 'global_hook'):
    from cloudpickle.cloudpickle_fast import *
else:
    from cloudpickle.cloudpickle import *

__version__ = '1.0.0'
