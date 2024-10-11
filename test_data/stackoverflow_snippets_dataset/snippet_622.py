# Extracted from https://stackoverflow.com/questions/183853/what-is-the-difference-between-and-when-used-for-division
import math
N = 1004291331219602346 # huge number 

print(N//100) #=> 10042913312196023 is correct answer
print(math.floor(N/100)) #=> 10042913312196024 is wrong answer
print(math.ceil(N/100)) #=> 10042913312196024 is wrong answer
print(int(N/100)) #=> 10042913312196024 is wrong answer

