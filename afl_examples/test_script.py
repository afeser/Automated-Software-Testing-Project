import sys

import afl

from cryptography.hazmat.primitives.asymmetric.utils import (
    decode_rfc6979_signature
)

afl.init()

try:
    decode_rfc6979_signature(sys.stdin.read())
except ValueError:
    pass
