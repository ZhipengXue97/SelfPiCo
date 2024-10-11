# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
with pytest.raises(
    ParserError, match="No result from selected items in iterparse."
):
    read_xml(
        xml_books,
        parser=parser,
        iterparse={"node": ["attr1", "elem1", "elem2", "elem3"]},
    )
