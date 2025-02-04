"""
PyTweet
~~~~~~~

PyTweet is a Synchronous python API wrapper for Twitter's API!

:copyright: (c) 2021-present TheFarGG & TheGenocides
:license: MIT, see LICENSE for more details.
"""
import logging
from typing import Literal, NamedTuple

from .dataclass import *
from .attachments import *
from .auth import *
from .client import *
from .entities import *
from .enums import *
from .environment import *
from .errors import *
from .events import *
from .constants import *
from .http import *
from .list import *
from .message import *
from .metrics import *
from .objects import *
from .paginations import *
from .parsers import *
from .relations import *
from .space import *
from .stream import *
from .tweet import *
from .user import *
from .utils import *

__title__ = "PyTweet"
__version__ = "1.5.0a10"
__author__ = "TheFarGG & TheGenocides"
__license__ = "MIT"
__copyright__ = "Copyright 2021-present TheFarGG & TheGenocides"


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=1, minor=5, micro=0, releaselevel="alpha", serial=10)

logging.getLogger(__name__).addHandler(logging.NullHandler())

assert version_info.releaselevel in (
    "alpha",
    "beta",
    "candidate",
    "final",
), "Invalid release level given."
