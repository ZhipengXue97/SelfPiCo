# Extracted from ./data/repos/scrapy/scrapy/mail.py
self.smtphost = smtphost
self.smtpport = smtpport
self.smtpuser = _to_bytes_or_none(smtpuser)
self.smtppass = _to_bytes_or_none(smtppass)
self.smtptls = smtptls
self.smtpssl = smtpssl
self.mailfrom = mailfrom
self.debug = debug
