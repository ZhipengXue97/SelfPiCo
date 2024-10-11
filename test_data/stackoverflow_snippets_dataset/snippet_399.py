# Extracted from https://stackoverflow.com/questions/5998245/how-do-i-get-the-current-time-in-milliseconds-in-python
def TimestampMillisec64():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000) 

