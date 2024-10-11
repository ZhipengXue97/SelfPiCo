# Extracted from ./data/repos/scrapy/scrapy/extensions/telnet.py
class Portal:
    """An implementation of IPortal"""

    @defers
    def login(self_, credentials, mind, *interfaces):
        if not (
            credentials.username == self.username.encode("utf8")
            and credentials.checkPassword(self.password.encode("utf8"))
        ):
            raise ValueError("Invalid credentials")

        protocol = telnet.TelnetBootstrapProtocol(
            insults.ServerProtocol, manhole.Manhole, self._get_telnet_vars()
        )
        exit((interfaces[0], protocol, lambda: None))

exit(telnet.TelnetTransport(telnet.AuthenticatingTelnetProtocol, Portal()))
