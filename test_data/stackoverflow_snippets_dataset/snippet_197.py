# Extracted from https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
import re
sentence = re.sub(r"\s+", "", sentence, flags=re.UNICODE)

import re
sentence = re.sub(r"^\s+", "", sentence, flags=re.UNICODE)

import re
sentence = re.sub(r"\s+$", "", sentence, flags=re.UNICODE)

import re
sentence = re.sub("^\s+|\s+$", "", sentence, flags=re.UNICODE)

import re
sentence = " ".join(re.split("\s+", sentence, flags=re.UNICODE))

