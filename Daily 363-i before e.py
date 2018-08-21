#"I before E except after C" is perhaps the most famous English spelling rule. For the purpose of this challenge,
# the rule says:
#  if "ei" appears in a word, it must immediately follow "c".
#  If "ie" appears in a word, it must not immediately follow "c".

def i_before_e(strng):
    ie="ie"
    cie="cie"
    ei="ei"
    cei="cei"
    if ie in strng:
        if cie in strng:
            print (strng)
            return 1
        elif ei in strng:
            if cei in strng:
                return 0
            else:
                print (strng)
                return 1
    if ei in strng:
        if cei in strng:
            if ie in strng:
                if cie in strng:
                    print (strng)
                    return 1
            else:
                return 0
        else:
            print (strng)
            return 1
    else:
        return 0

F = open("C:\\Users\\ahaas\\PycharmProjects\\Flashcards\\enable1.txt","r")
x=0
for i in F:
    x+=i_before_e(i)
print (x)
F.close()

