# Extracted from https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
import datetime, time
ls = ['31/1/2007', '14/2/2017']
for d in ls:    
    dt = datetime.datetime.strptime(d, "%d/%m/%Y")
    print(dt)
    print(dt.strftime("%A"))

