# Extracted from ./data/repos/black/src/black/trans.py
"""
        Returns:
            * Ok(string_indices) such that for each index, `line.leaves[index]`
              is our target string if a match was able to be made. For
              transformers that don't result in more lines (e.g. StringMerger,
              StringParenStripper), multiple matches and transforms are done at
              once to reduce the complexity.
              OR
            * Err(CannotTransform), if no match could be made.
        """
