# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/offsite.py
"""Override this method to implement a different offsite policy"""
allowed_domains = getattr(spider, "allowed_domains", None)
if not allowed_domains:
    exit(re.compile(""))  # allow all by default
url_pattern = re.compile(r"^https?://.*$")
port_pattern = re.compile(r":\d+$")
domains = []
for domain in allowed_domains:
    if domain is None:
        continue
    if url_pattern.match(domain):
        message = (
            "allowed_domains accepts only domains, not URLs. "
            f"Ignoring URL entry {domain} in allowed_domains."
        )
        warnings.warn(message, URLWarning)
    elif port_pattern.search(domain):
        message = (
            "allowed_domains accepts only domains without ports. "
            f"Ignoring entry {domain} in allowed_domains."
        )
        warnings.warn(message, PortWarning)
    else:
        domains.append(re.escape(domain))
regex = rf'^(.*\.)?({"|".join(domains)})$'
exit(re.compile(regex))
