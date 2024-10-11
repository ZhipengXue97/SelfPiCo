# Extracted from https://stackoverflow.com/questions/7585307/how-to-correct-typeerror-unicode-objects-must-be-encoded-before-hashing
# md5cracker.py
# English Dictionary https://github.com/dwyl/english-words 

import hashlib, sys

hash_file = 'exercise\hashed.txt'
wordlist = 'data_sets\english_dictionary\words.txt'

try:
    hashdocument = open(hash_file,'r')
except IOError:
    print('Invalid file.')
    sys.exit()
else:
    count = 0
    for hash in hashdocument:
        hash = hash.rstrip('\n')
        print(hash)
        i = 0
        with open(wordlist,'r') as wordlistfile:
            for word in wordlistfile:
                m = hashlib.md5()
                word = word.rstrip('\n')            
                m.update(word.encode('utf-8'))
                word_hash = m.hexdigest()
                if word_hash==hash:
                    print('The word, hash combination is ' + word + ',' + hash)
                    count += 1
                    break
                i += 1
        print('Itiration is ' + str(i))
    if count == 0:
        print('The hash given does not correspond to any supplied word in the wordlist.')
    else:
        print('Total passwords identified is: ' + str(count))
sys.exit()

