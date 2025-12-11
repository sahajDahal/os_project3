# Session 1 — 2025-12-09 10:21am

## Thoughts So Far

No major new thoughts, but I began setting up the core constants and helper functions needed for the project.

## Plan for This Session

- Define required constants (`BLOCK_SIZE`, `MAGIC`, `MIN_DEGREE`, `MAX_KEYS`, `MAX_CHILDREN`)
- Implement integer encoding helpers (`u64`, `read_u64`)
- Prepare to implement header and node block classes next session

# Session 2 — 2025-12-09 12:50pm

## Thoughts So Far

Now that the header structure is implemented, the overall file layout feels clearer. The next major piece will be node serialization.

## Plan for This Session

- Implement the `IndexHeader` class
- Add `load` and `save` methods for reading/writing the 512-byte header block
- Ensure the magic number and block fields follow the specification

# session 3 — 2025-12-10 6:24pm

## Thoughts So Far

Implementing the node block structure clarified how the file-based B-tree will operate. Reading and writing entire nodes at fixed offsets is now straightforward.

## Plan for This Session

- Implement the `BTreeNode` class with in-memory fields
- Add `load` and `save` methods for full 512-byte node serialization
- Ensure keys, values, and child pointers follow the required fixed-size layout

# session 4 — 2025-12-010 6:30pm

## Thoughts So Far

The command layer is now structured, and each operation has a placeholder. This makes it easier to progressively integrate B-tree logic later.

## Plan for This Session

- Add command functions (`create`, `insert`, `search`, `print`, `extract`, `load`)
- Ensure each command loads the index header correctly
- Set up placeholders where B-tree operations will eventually plug in
