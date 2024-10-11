# Extracted from https://stackoverflow.com/questions/5055042/whats-the-best-practice-using-a-settings-file-in-python
import json
config = {'handler' : 'adminhandler.py', 'timeoutsec' : 5 }
json.dump(config, open('/tmp/config.json', 'w'))
json.load(open('/tmp/config.json'))   
{u'handler': u'adminhandler.py', u'timeoutsec': 5}

