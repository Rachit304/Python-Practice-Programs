import re
def LoveForFrenchFries(str1,word):
        str1.lower()
        length= len(re.findall(word, str1))
        print("Repetation is ", length)


def MyScottishAccent(str1, old, new):
    str1.lower()
    str1 = re.sub(old, new, str1)
    print(str1)


def LinkVowels(str1):
    pattern = '.+[aeiouAEIOU]\s[aeiouAEIOU]+.'

    if re.search(pattern, str1):
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













