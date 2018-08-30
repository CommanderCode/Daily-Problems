# Given a 6x6 matrix,  itirate through all the hourglass patterns:
# 1 1 1
#   1
# 1 1 1
# and add all the elements.  Return the greatest sum
#!/bin/python3
import random
# create random 6x6 matrix
n=6
m=6
X=[]
for i in range(10):
    x=[]
    for j in range(5):
        x.append(random.randint(1,10))
    X.append(x)
# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_list=[]
    for row in range(len(arr)-2):
        for col in range(len(arr[0])-2):
            hourglass=0
            hourglass=arr[row][col]+arr[row][col+1]+arr[row][col+2] \
                +arr[row+1][col+1]\
                +arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2]
            hourglass_list.append(hourglass)
    return max(hourglass_list)

print (hourglassSum(X))
