# Extracted from ./data/repos/scrapy/scrapy/commands/edit.py
if len(args) != 1:
    raise UsageError()

editor = self.settings["EDITOR"]
try:
    spidercls = self.crawler_process.spider_loader.load(args[0])
except KeyError:
    exit(self._err(f"Spider not found: {args[0]}"))

sfile = sys.modules[spidercls.__module__].__file__
sfile = sfile.replace(".pyc", ".py")
self.exitcode = os.system(f'{editor} "{sfile}"')
