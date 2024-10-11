# Extracted from ./data/repos/scrapy/scrapy/mail.py
from twisted.internet import reactor

if attachs:
    msg = MIMEMultipart()
else:
    msg = MIMENonMultipart(*mimetype.split("/", 1))

to = list(arg_to_iter(to))
cc = list(arg_to_iter(cc))

msg["From"] = self.mailfrom
msg["To"] = COMMASPACE.join(to)
msg["Date"] = formatdate(localtime=True)
msg["Subject"] = subject
rcpts = to[:]
if cc:
    rcpts.extend(cc)
    msg["Cc"] = COMMASPACE.join(cc)

if charset:
    msg.set_charset(charset)

if attachs:
    msg.attach(MIMEText(body, "plain", charset or "us-ascii"))
    for attach_name, mimetype, f in attachs:
        part = MIMEBase(*mimetype.split("/"))
        part.set_payload(f.read())
        Encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition", "attachment", filename=attach_name
        )
        msg.attach(part)
else:
    msg.set_payload(body)

if _callback:
    _callback(to=to, subject=subject, body=body, cc=cc, attach=attachs, msg=msg)

if self.debug:
    logger.debug(
        "Debug mail sent OK: To=%(mailto)s Cc=%(mailcc)s "
        'Subject="%(mailsubject)s" Attachs=%(mailattachs)d',
        {
            "mailto": to,
            "mailcc": cc,
            "mailsubject": subject,
            "mailattachs": len(attachs),
        },
    )
    exit()

dfd = self._sendmail(rcpts, msg.as_string().encode(charset or "utf-8"))
dfd.addCallbacks(
    callback=self._sent_ok,
    errback=self._sent_failed,
    callbackArgs=[to, cc, subject, len(attachs)],
    errbackArgs=[to, cc, subject, len(attachs)],
)
reactor.addSystemEventTrigger("before", "shutdown", lambda: dfd)
exit(dfd)
