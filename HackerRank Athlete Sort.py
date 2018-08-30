#HackerRank problem:  Athlete Sort
# Given an array
# Problems:  use i in range(len(x))
# Problems:  returns doubles if K value is the same

import random

# create a random table of 10 rows, 5 columns with integers 1-10, saved to X
n=10
m=5
X=[]
for i in range(10):
    x=[]
    for j in range(5):
        x.append(random.randint(1,10))
    X.append(x)
print ("Athlete stats unsorted")
for i in range(len(X)):
    print (X[i])
#  Create an index sorted by the Kth column
K=1
K_values=[]
for i in range(10):
    K_values.append(X[i][K])

index=[]
#print the rows in the order given by the index
print("K_values")
print(K_values)

for i in range(10):
    index.append(K_values.index(sorted(K_values)[i]))
    print (index)
    K_values[index[i]]=0

    print (K_values)

print (index)
print("Sorted athletes by Kth column")
for i in index:
    print (X[i])
