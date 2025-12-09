import sys
import struct
import os

BLOCK_SIZE = 512
MAGIC = b"4348PRJ3"
MIN_DEGREE = 10   # t = 10
MAX_KEYS = 2 * MIN_DEGREE - 1  # = 19 keys
MAX_CHILDREN = MAX_KEYS + 1    # = 20

def u64(n):
    return n.to_bytes(8, "big")

def read_u64(b):
    return int.from_bytes(b, "big")