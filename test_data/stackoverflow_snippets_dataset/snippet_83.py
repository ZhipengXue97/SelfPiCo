# Extracted from https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-represents-a-number-float-or-int
"1221323".isdigit()
True

"12.34".isdigit()
False
"12.34".replace('.','',1).isdigit()
True
"12.3.4".replace('.','',1).isdigit()
False

'-12'.lstrip('-')
'12'

'-12.34'.lstrip('-').replace('.','',1).isdigit()
True
'.-234'.lstrip('-').replace('.','',1).isdigit()
False

