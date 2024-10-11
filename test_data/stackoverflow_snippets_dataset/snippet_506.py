# Extracted from https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list
from scipy import stats
l = [15, 18, 2, 36, 12, 78, 5, 6, 9]
print(stats.describe(l))

# DescribeResult(nobs=9, minmax=(2, 78), mean=20.11111111111111, 
# variance=572.3611111111111, skewness=1.7791785448425341, 
# kurtosis=1.9422716419666397)

