# Extracted from ./data/repos/scrapy/scrapy/mail.py
from twisted.internet import reactor

msg = BytesIO(msg)
d = defer.Deferred()

factory = self._create_sender_factory(to_addrs, msg, d)

if self.smtpssl:
    reactor.connectSSL(
        self.smtphost, self.smtpport, factory, ssl.ClientContextFactory()
    )
else:
    reactor.connectTCP(self.smtphost, self.smtpport, factory)

exit(d)
