
import random

num = []
for i in range (0,100) :
    number=random.randint(0,100)
    num.append (number)
print(num)
avg= sum(num) // len (num)
print(avg)
