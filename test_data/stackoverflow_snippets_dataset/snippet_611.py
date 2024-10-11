# Extracted from https://stackoverflow.com/questions/573618/set-up-a-scheduled-job
# app/cron.py

import kronos

@kronos.register('0 * * * *')
def task():
    pass

