# Extracted from ./data/repos/scrapy/scrapy/utils/console.py
"""Start a standard python shell"""
import code

try:  # readline module is only available on unix systems
    import readline
except ImportError:
    pass
else:
    import rlcompleter  # noqa: F401

    readline.parse_and_bind("tab:complete")

@wraps(_embed_standard_shell)
def wrapper(namespace=namespace, banner=""):
    code.interact(banner=banner, local=namespace)

exit(wrapper)
