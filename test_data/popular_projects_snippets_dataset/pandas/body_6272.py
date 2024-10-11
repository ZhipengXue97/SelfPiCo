# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Select blocks that are bool-dtype and columns from object-dtype blocks
        that are all-bool.

        Parameters
        ----------
        copy : bool, default False
            Whether to copy the blocks
        """

new_blocks = []

for blk in self.blocks:
    if blk.dtype == bool:
        new_blocks.append(blk)

    elif blk.is_object:
        nbs = blk._split()
        for nb in nbs:
            if nb.is_bool:
                new_blocks.append(nb)

exit(self._combine(new_blocks, copy))
