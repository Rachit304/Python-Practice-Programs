import re
def LoveForFrenchFries(Str1, Word):
    space =" "
    if space in Str1:
        print("Please Enter Continuous String")
    else:
        length= len(re.findall(Word, Str1))
        print(Word, " is Repeated ", length, " times")


def MyScottishAccent(Str1, Old, New):
    Str1 = re.sub(Old, New, Str1)
    print("Scottish will say like ", Str1)


def LinkVowels(Str1):
    pattern = r'.+[aeiouAEIOU]\s[aeiouAEIOU]+.'

    if re.search(pattern, Str1):
        print("Ur String is a Link vowel type")
    else:
        print("Ur String is not a Link vowel type")


def LonelyOnes(strOne):

    one = re.findall("(?<!1)1(?!1)", strOne)
    return len(one)


str1 = input("Please Enter a String:- ")
word = input("Please enter the word to search :- ")
LoveForFrenchFries(str1, word)

str1 = input("Please Enter another String:- ")
old = input("Enter the word  you want to replace :  ")
new = input("Enter the word you want to replace with: ")
MyScottishAccent(str1, old, new)

LinkVowels(str1)
print(LonelyOnes(input("enter a num :- ")))
