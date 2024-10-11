# Extracted from https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))

''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(N))

