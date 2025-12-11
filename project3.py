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

# -------------------------------------------------------------------
# B-TREE NODE BLOCK
# -------------------------------------------------------------------
class BTreeNode:
    def __init__(self, block_id, parent_id=0):
        self.block_id = block_id
        self.parent_id = parent_id
        self.keys = []
        self.values = []
        self.children = []

    @staticmethod
    def load(f, block_id):
        f.seek(block_id * BLOCK_SIZE)
        raw = f.read(BLOCK_SIZE)

        node = BTreeNode(
            read_u64(raw[0:8]),
            read_u64(raw[8:16])
        )

        num_keys = read_u64(raw[16:24])

        # Load keys
        idx = 24
        for _ in range(MAX_KEYS):
            k = read_u64(raw[idx:idx+8])
            idx += 8
            if k != 0:
                node.keys.append(k)

        # Load values
        for _ in range(MAX_KEYS):
            v = read_u64(raw[idx:idx+8])
            idx += 8
            if v != 0:
                node.values.append(v)

        # Load child pointers
        for _ in range(MAX_CHILDREN):
            c = read_u64(raw[idx:idx+8])
            idx += 8
            if c != 0:
                node.children.append(c)

        return node

    def save(self, f):
        block = bytearray(BLOCK_SIZE)

        # Basic info
        block[0:8] = u64(self.block_id)
        block[8:16] = u64(self.parent_id)
        block[16:24] = u64(len(self.keys))

        idx = 24

        # Write keys (pad with 0)
        for i in range(MAX_KEYS):
            v = self.keys[i] if i < len(self.keys) else 0
            block[idx:idx+8] = u64(v)
            idx += 8

        # Write values
        for i in range(MAX_KEYS):
            v = self.values[i] if i < len(self.values) else 0
            block[idx:idx+8] = u64(v)
            idx += 8

        # Write children
        for i in range(MAX_CHILDREN):
            v = self.children[i] if i < len(self.children) else 0
            block[idx:idx+8] = u64(v)
            idx += 8

        f.seek(self.block_id * BLOCK_SIZE)
        f.write(block)