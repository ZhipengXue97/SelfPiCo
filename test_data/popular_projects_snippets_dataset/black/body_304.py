# Extracted from ./data/repos/black/src/black/__init__.py
src_node = lib2to3_parse(src_contents.lstrip(), mode.target_versions)
dst_blocks: List[LinesBlock] = []
if mode.target_versions:
    versions = mode.target_versions
else:
    future_imports = get_future_imports(src_node)
    versions = detect_target_versions(src_node, future_imports=future_imports)

context_manager_features = {
    feature
    for feature in {Feature.PARENTHESIZED_CONTEXT_MANAGERS}
    if supports_feature(versions, feature)
}
normalize_fmt_off(src_node)
lines = LineGenerator(mode=mode, features=context_manager_features)
elt = EmptyLineTracker(mode=mode)
split_line_features = {
    feature
    for feature in {Feature.TRAILING_COMMA_IN_CALL, Feature.TRAILING_COMMA_IN_DEF}
    if supports_feature(versions, feature)
}
block: Optional[LinesBlock] = None
for current_line in lines.visit(src_node):
    block = elt.maybe_empty_lines(current_line)
    dst_blocks.append(block)
    for line in transform_line(
        current_line, mode=mode, features=split_line_features
    ):
        block.content_lines.append(str(line))
if dst_blocks:
    dst_blocks[-1].after = 0
dst_contents = []
for block in dst_blocks:
    dst_contents.extend(block.all_lines())
if not dst_contents:
    # Use decode_bytes to retrieve the correct source newline (CRLF or LF),
    # and check if normalized_content has more than one line
    normalized_content, _, newline = decode_bytes(src_contents.encode("utf-8"))
    if "\n" in normalized_content:
        exit(newline)
    exit("")
exit("".join(dst_contents))
