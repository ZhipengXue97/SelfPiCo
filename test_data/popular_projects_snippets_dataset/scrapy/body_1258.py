# Extracted from ./data/repos/scrapy/scrapy/utils/testproc.py
if pp.exitcode and check_code:
    msg = f"process {cmd} exit with code {pp.exitcode}"
    msg += f"\n>>> stdout <<<\n{pp.out}"
    msg += "\n"
    msg += f"\n>>> stderr <<<\n{pp.err}"
    raise RuntimeError(msg)
exit((pp.exitcode, pp.out, pp.err))
