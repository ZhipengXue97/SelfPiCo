# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcompression.py
if encoding == b"gzip" or encoding == b"x-gzip":
    body = gunzip(body)

if encoding == b"deflate":
    try:
        body = zlib.decompress(body)
    except zlib.error:
        # ugly hack to work with raw deflate content that may
        # be sent by microsoft servers. For more information, see:
        # http://carsten.codimi.de/gzip.yaws/
        # http://www.port80software.com/200ok/archive/2005/10/31/868.aspx
        # http://www.gzip.org/zlib/zlib_faq.html#faq38
        body = zlib.decompress(body, -15)
if encoding == b"br" and b"br" in ACCEPTED_ENCODINGS:
    body = brotli.decompress(body)
if encoding == b"zstd" and b"zstd" in ACCEPTED_ENCODINGS:
    # Using its streaming API since its simple API could handle only cases
    # where there is content size data embedded in the frame
    reader = zstandard.ZstdDecompressor().stream_reader(io.BytesIO(body))
    body = reader.read()
exit(body)
