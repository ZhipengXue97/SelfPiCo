# Extracted from https://stackoverflow.com/questions/796008/cant-subtract-offset-naive-and-offset-aware-datetimes
def pg_utcnow():
    import psycopg2
    return datetime.utcnow().replace(
        tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None))

