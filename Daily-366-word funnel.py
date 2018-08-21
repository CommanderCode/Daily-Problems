#Given two strings of letters, determine whether the second can be made from the first by removing one letter.
# The remaining letters must stay in the same order.

def funnel(a,b):
    for i in range(len(a)):
        a_list=list(a)
        del a_list[i]
        a_new="".join(a_list)
        if a_new==b:
            return True
            break
    return False
print (funnel("leave", "eave"))
print (funnel("reset", "rest"))
print (funnel("dragoon", "dragon"))
print (funnel("eave", "leave") )
print (funnel("sleet", "lets"))
print (funnel("skiff", "ski"))

#Given a string, find all words from the enable1 word list that can be made by removing one letter from the string.
# If there are two possible letters you can remove to make the same word, only count it once. Ordering of the output
# words doesn't matter.


def funnel_bonus_1(a):
    F = open("C:\\Users\\ahaas\\PycharmProjects\\Daily Problems\\enable1.txt","r")
    words=[]
    for line in F:
        line=line.replace("\n","")
        if funnel(a,line):
            words.append(line)
    print (words)
    F.close()
funnel_bonus_1("dragoon")
funnel_bonus_1("boats")
funnel_bonus_1("affidavit")
