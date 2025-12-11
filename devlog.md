# Session 1 — 2025-12-09 10:21am

## Thoughts So Far

No major new thoughts, but I began setting up the core constants and helper functions needed for the project.

## Plan for This Session

- Define required constants (`BLOCK_SIZE`, `MAGIC`, `MIN_DEGREE`, `MAX_KEYS`, `MAX_CHILDREN`)
- Implement integer encoding helpers (`u64`, `read_u64`)
- Prepare to implement header and node block classes next session

---

# Session 2 — 2025-12-09 12:50pm

## Thoughts So Far

Now that the header structure is implemented, the overall file layout feels clearer. The next major piece will be node serialization.

## Plan for This Session

- Implement the `IndexHeader` class
- Add `load` and `save` methods for reading/writing the 512-byte header block
- Ensure the magic number and block fields follow the specification

---

# Session 3 — 2025-12-10 6:24pm

## Thoughts So Far

Implementing the node block structure clarified how the file-based B-tree will operate. Reading and writing entire nodes at fixed offsets is now straightforward.

## Plan for This Session

- Implement the `BTreeNode` class with in-memory fields
- Add `load` and `save` methods for full 512-byte node serialization
- Ensure keys, values, and child pointers follow the required fixed-size layout

---

# Session 4 — 2025-12-10 6:30pm

## Thoughts So Far

The command layer is now structured, and each operation has a placeholder. This makes it easier to progressively integrate B-tree logic later.

## Plan for This Session

- Add command functions (`create`, `insert`, `search`, `print`, `extract`, `load`)
- Ensure each command loads the index header correctly
- Set up placeholders where B-tree operations will eventually plug in

---

# Session 5 — 2025-12-10 6:35pm

## Thoughts So Far

The program is now runnable from the command line, and all commands are properly routed. This completes the basic structure before implementing real B-tree logic.

## Plan for This Session

- Implement the main function to parse commands and forward arguments
- Ensure each supported command is handled cleanly
- Provide a default usage message for incorrect invocation

---

# Session 6 — 2025-12-10 6:50pm

## Thoughts So Far

Now that the high-level command framework is complete, I’m realizing how important clean separation between B-tree logic and file operations will be.

## Plan for This Session

- Outline where B-tree insert logic will go
- Sketch pseudocode for search and traversal
- Ensure the command functions are ready for full integration

---

# Session 7 — 2025-12-10 7:05pm

## Thoughts So Far

Starting to think more about node splitting and how to maintain the “only 3 nodes in memory” rule. This will require careful sequencing when navigating the tree.

## Plan for This Session

- Draft the structure for insert with splitting (not yet implementing)
- Identify which nodes must be read during insert
- Decide how to update parents correctly via file offsets

---

# Session 8 — 2025-12-10 7:20pm

## Thoughts So Far

Traversal for the `print` and `extract` commands will require an in-order walk, even though the nodes are stored arbitrarily in blocks. This reinforces the need to keep child pointers correct.

## Plan for This Session

- Design in-order traversal algorithm using file-based nodes
- Determine how to minimize nodes in memory during traversal
- Plan the output format for print and extract

---

# Session 9 — 2025-12-10 7:35pm

## Thoughts So Far

Considering validation tests helped clarify expectations around duplicate keys, invalid files, and CSV formatting. This will make debugging easier once B-tree logic is implemented.

## Plan for This Session

- Document expected behavior for each command
- Create a testing checklist for all standard and edge cases
- Ensure error handling is consistent across commands

---

# Session 10 — 2025-12-10 7:50pm

## Thoughts So Far

Everything is now in place structurally. The next major step is implementing the actual B-tree mechanics, which will be the hardest part but now feels more manageable.

## Plan for This Session

- Begin implementing basic B-tree search (no splits)
- Plan key insertion ordering logic
- Prepare to integrate split logic in a later session
