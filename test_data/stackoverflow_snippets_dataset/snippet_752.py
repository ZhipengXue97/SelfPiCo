# Extracted from https://stackoverflow.com/questions/2600775/how-to-get-week-number-in-python
testdate=datetime.datetime(2010,6,16)
print(((testdate - datetime.datetime(testdate.year,1,1)).days // 7) + 1)
24

