# Extracted from https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile
Regx3GList = re.search("(WCDMA:)((\d*)(,?))*", txt, re.IGNORECASE)

Regx3GList = re.search("**(?i)**(WCDMA:)((\d*)(,?))*", txt)

