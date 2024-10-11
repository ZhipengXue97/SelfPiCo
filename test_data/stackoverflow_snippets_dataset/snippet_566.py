# Extracted from https://stackoverflow.com/questions/6871016/adding-days-to-a-date-in-python
class GetDate:
    def __init__(self, date, format="%Y-%m-%d"):
        self.tz = pytz.timezone("Europe/Warsaw")

        if isinstance(date, str):
            date = datetime.strptime(date, format)

        self.date = date.astimezone(self.tz)

    def time_delta_days(self, days):
        return self.date + timedelta(days=days)

    def time_delta_hours(self, hours):
        return self.date + timedelta(hours=hours)

    def time_delta_seconds(self, seconds):
        return self.date + timedelta(seconds=seconds)

    def get_minimum_time(self):
        return datetime.combine(self.date, time.min).astimezone(self.tz)

    def get_maximum_time(self):
        return datetime.combine(self.date, time.max).astimezone(self.tz)

    def get_month_first_day(self):
        return datetime(self.date.year, self.date.month, 1).astimezone(self.tz)

    def current(self):
        return self.date

    def get_month_last_day(self):
        lastDay = calendar.monthrange(self.date.year, self.date.month)[1]
        date = datetime(self.date.year, self.date.month, lastDay)
        return datetime.combine(date, time.max).astimezone(self.tz)

