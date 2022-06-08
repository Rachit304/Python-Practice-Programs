import OMG

str1 = input("Are You Scared(yes/no) ? -  ")
str1 = str1.lower()
if str1 == 'yes':
    bool1 = True
    OMG.AllisWell(bool1)
elif str1 == 'no':
    bool1 = False
    OMG.AllisWell(bool1)
