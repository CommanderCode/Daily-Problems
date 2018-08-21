A = open("C:\\Users\\ahaas\\PycharmProjects\\Flashcards\\exceptionsAndy.txt","r")
B = open("C:\\Users\\ahaas\\PycharmProjects\\Flashcards\\exceptionsBen.txt","r")

#or, readlines reads the individual line into a list
A_by_line =A.readlines()
B_by_line =B.readlines()

Number_of_differences=0
j=0
for i in range(len(B_by_line)):
    if B_by_line[i]!= A_by_line[j]:
        print (B_by_line[i])
        Number_of_differences+=1
        j+=-1
    j+=1
print(Number_of_differences)
