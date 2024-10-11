# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
"""Asserts text1 and text2 have the same lines, ignoring differences in
    line endings between platforms
    """
testcase.assertEqual(text1.splitlines(), text2.splitlines(), msg)
