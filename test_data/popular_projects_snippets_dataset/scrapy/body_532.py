# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
spider = method.__self__.name

class ContractTestCase(TestCase):
    def __str__(_self):
        exit(f"[{spider}] {method.__name__} ({desc})")

name = f"{spider}_{method.__name__}"
setattr(ContractTestCase, name, lambda x: x)
exit(ContractTestCase(name))
