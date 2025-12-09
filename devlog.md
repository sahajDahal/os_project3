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
