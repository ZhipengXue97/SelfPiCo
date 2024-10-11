# Extracted from https://stackoverflow.com/questions/237079/how-do-i-get-file-creation-and-modification-date-times
import pathlib
fname = pathlib.Path('test.py')
assert fname.exists(), f'No such file: {fname}'  # check that the file exists
print(fname.stat())
os.stat_result(st_mode=33206, st_ino=5066549581564298, st_dev=573948050, st_nlink=1, st_uid=0, st_gid=0, st_size=413, st_atime=1523480272, st_mtime=1539787740, st_ctime=1523480272)

import datetime
mtime = datetime.datetime.fromtimestamp(fname.stat().st_mtime, tz=datetime.timezone.utc)
print(mtime)
datetime.datetime(2018, 10, 17, 10, 49, 0, 249980)

ctime = datetime.datetime.fromtimestamp(fname.stat().st_ctime, tz=datetime.timezone.utc)
print(ctime)
datetime.datetime(2018, 4, 11, 16, 57, 52, 151953)

