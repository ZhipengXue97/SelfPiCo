# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
# make mypy happy
assert self.how != "cross"
left_ax = self.left.index
right_ax = self.right.index

if self.left_index and self.right_index and self.how != "asof":
    join_index, left_indexer, right_indexer = left_ax.join(
        right_ax, how=self.how, return_indexers=True, sort=self.sort
    )

elif self.right_index and self.how == "left":
    join_index, left_indexer, right_indexer = _left_join_on_index(
        left_ax, right_ax, self.left_join_keys, sort=self.sort
    )

elif self.left_index and self.how == "right":
    join_index, right_indexer, left_indexer = _left_join_on_index(
        right_ax, left_ax, self.right_join_keys, sort=self.sort
    )
else:
    (left_indexer, right_indexer) = self._get_join_indexers()

    if self.right_index:
        if len(self.left) > 0:
            join_index = self._create_join_index(
                left_ax,
                right_ax,
                left_indexer,
                how="right",
            )
        else:
            join_index = right_ax.take(right_indexer)
    elif self.left_index:
        if self.how == "asof":
            # GH#33463 asof should always behave like a left merge
            join_index = self._create_join_index(
                left_ax,
                right_ax,
                left_indexer,
                how="left",
            )

        elif len(self.right) > 0:
            join_index = self._create_join_index(
                right_ax,
                left_ax,
                right_indexer,
                how="left",
            )
        else:
            join_index = left_ax.take(left_indexer)
    else:
        join_index = default_index(len(left_indexer))

if len(join_index) == 0 and not isinstance(join_index, MultiIndex):
    join_index = default_index(0).set_names(join_index.name)
exit((join_index, left_indexer, right_indexer))
