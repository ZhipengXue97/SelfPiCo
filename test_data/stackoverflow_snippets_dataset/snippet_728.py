# Extracted from https://stackoverflow.com/questions/12595051/check-if-string-matches-pattern
def is_match(pattern, string, flags=re.IGNORECASE | re.DOTALL): # or "is_full_match", as desired
    return re.fullmatch(pattern, string, flags)!=None

