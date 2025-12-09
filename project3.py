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
# -------------------------------------------------------------------
# INDEX FILE HEADER
# -------------------------------------------------------------------
class IndexHeader:
    def __init__(self, root_id=0, next_id=1):
        self.root_id = root_id
        self.next_id = next_id

    @staticmethod
    def load(f):
        block = f.read(BLOCK_SIZE)
        if block[:8] != MAGIC:
            raise ValueError("Invalid index file format")

        root_id = read_u64(block[8:16])
        next_id = read_u64(block[16:24])
        return IndexHeader(root_id, next_id)

    def save(self, f):
        block = bytearray(BLOCK_SIZE)
        block[:8] = MAGIC
        block[8:16] = u64(self.root_id)
        block[16:24] = u64(self.next_id)
        f.seek(0)
        f.write(block)