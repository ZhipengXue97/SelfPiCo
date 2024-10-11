# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
"""Upload file to S3 storage"""
key_name = f"{self.prefix}{path}"
buf.seek(0)
extra = self._headers_to_botocore_kwargs(self.HEADERS)
if headers:
    extra.update(self._headers_to_botocore_kwargs(headers))
exit(threads.deferToThread(
    self.s3_client.put_object,
    Bucket=self.bucket,
    Key=key_name,
    Body=buf,
    Metadata={k: str(v) for k, v in (meta or {}).items()},
    ACL=self.POLICY,
    **extra,
))
