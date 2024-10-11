# Extracted from https://stackoverflow.com/questions/127803/how-do-i-parse-an-iso-8601-formatted-date
class FixedOffset(tzinfo):
    """Fixed offset in minutes: `time = utc_time + utc_offset`."""
    def __init__(self, offset):
        self.__offset = timedelta(minutes=offset)
        hours, minutes = divmod(offset, 60)
        #NOTE: the last part is to remind about deprecated POSIX GMT+h timezones
        #  that have the opposite sign in the name;
        #  the corresponding numeric value is not used e.g., no minutes
        self.__name = '<%+03d%02d>%+d' % (hours, minutes, -hours)
    def utcoffset(self, dt=None):
        return self.__offset
    def tzname(self, dt=None):
        return self.__name
    def dst(self, dt=None):
        return timedelta(0)
    def __repr__(self):
        return 'FixedOffset(%d)' % (self.utcoffset().total_seconds() / 60)
    def __getinitargs__(self):
        return (self.__offset.total_seconds()/60,)

def parse_isoformat_datetime(isodatetime):
    try:
        return datetime.strptime(isodatetime, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        pass
    try:
        return datetime.strptime(isodatetime, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        pass
    pat = r'(.*?[+-]\d{2}):(\d{2})'
    temp = re.sub(pat, r'\1\2', isodatetime)
    naive_date_str = temp[:-5]
    offset_str = temp[-5:]
    naive_dt = datetime.strptime(naive_date_str, '%Y-%m-%dT%H:%M:%S.%f')
    offset = int(offset_str[-4:-2])*60 + int(offset_str[-2:])
    if offset_str[0] == "-":
        offset = -offset
    return naive_dt.replace(tzinfo=FixedOffset(offset))

