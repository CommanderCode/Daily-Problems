# def rot_once(a):
#     a_new = list(range(len(a)))
#
#     a_new[len(a_new)-1]=a[0]
#     for j in range(len(a)-1):
#         a_new[j]=a[j+1]
#     return a_new
# def rotLeft(a, d):
#     count=0
#     while count< d:
#         count+=1
#         a=rot_once(a)
#     return a

def rotLeft(a,d):


a=[1,2,3,4,5]
d=3
result=rotLeft(a,d)
print (result)
