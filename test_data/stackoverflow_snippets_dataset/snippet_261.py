# Extracted from https://stackoverflow.com/questions/2186525/how-to-use-glob-to-find-files-recursively
from fsspec.implementations.zip import ZipFileSystem
fs = ZipFileSystem("/tmp/test.zip")
fs.glob("/**")  # equivalent: fs.find("/")

from s3fs import S3FileSystem
fs_s3 = S3FileSystem(anon=True)
fs_s3.glob("noaa-goes16/ABI-L1b-RadF/2020/045/**")  # or use fs_s3.find

from fsspec.implementations.local import LocalFileSystem
fs = LocalFileSystem()
fs.glob("/tmp/test/**")

