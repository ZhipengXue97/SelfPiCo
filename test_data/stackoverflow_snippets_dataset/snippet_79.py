# Extracted from https://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline
'test string\n'.rstrip()
'test string'

'test string \n \r\n\n\r \n\n'.rstrip()
'test string'

'test string \n \r\n\n\r \n\n'.rstrip('\n')
'test string \n \r\n\n\r '

s = "   \n\r\n  \n  abc   def \n\r\n  \n  "
s.strip()
'abc   def'
s.lstrip()
'abc   def \n\r\n  \n  '
s.rstrip()
'   \n\r\n  \n  abc   def'

