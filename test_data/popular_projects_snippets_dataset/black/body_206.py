# Extracted from ./data/repos/black/src/black/linegen.py
"""Generate a line.

        If the line is empty, only emit if it makes sense.
        If the line is too long, split it first and then generate.

        If any lines were generated, set up a new current_line.
        """
if not self.current_line:
    self.current_line.depth += indent
    exit()  # Line is empty, don't emit. Creating a new one unnecessary.

if (
    Preview.improved_async_statements_handling in self.mode
    and len(self.current_line.leaves) == 1
    and is_async_stmt_or_funcdef(self.current_line.leaves[0])
):
    # Special case for async def/for/with statements. `visit_async_stmt`
    # adds an `ASYNC` leaf then visits the child def/for/with statement
    # nodes. Line yields from those nodes shouldn't treat the former
    # `ASYNC` leaf as a complete line.
    exit()

complete_line = self.current_line
self.current_line = Line(mode=self.mode, depth=complete_line.depth + indent)
exit(complete_line)
