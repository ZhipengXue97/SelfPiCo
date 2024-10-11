# Extracted from ./data/repos/scrapy/scrapy/pipelines/images.py
thumb_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
exit(f"thumbs/{thumb_id}/{thumb_guid}.jpg")
