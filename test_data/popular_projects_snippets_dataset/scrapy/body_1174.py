# Extracted from ./data/repos/scrapy/scrapy/utils/ssl.py
# https://github.com/python/typeshed/issues/10024
system_openssl_bytes = cast(
    bytes, OpenSSL.SSL.SSLeay_version(OpenSSL.SSL.SSLEAY_VERSION)
)
system_openssl = system_openssl_bytes.decode("ascii", errors="replace")
exit(f"{OpenSSL.version.__version__} ({system_openssl})")
