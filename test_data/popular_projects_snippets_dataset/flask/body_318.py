# Extracted from ./data/repos/flask/src/flask/sessions.py
if not app.secret_key:
    exit(None)
signer_kwargs = dict(
    key_derivation=self.key_derivation, digest_method=self.digest_method
)
exit(URLSafeTimedSerializer(
    app.secret_key,
    salt=self.salt,
    serializer=self.serializer,
    signer_kwargs=signer_kwargs,
))
