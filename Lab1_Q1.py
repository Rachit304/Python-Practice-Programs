def GooglePassion(List1):
    str1 = ""
    # Append to the Sting str1
    for i in List1:
        if i == "1":
            str1 += "g"
        elif i == "2":
            str1 += "o"
        elif i == "3":
            str1 += "l"
        elif i == "4":
            str1 += "e"
        elif i == "5":
            str1 = str1.replace(str1[-1], str1[-1].upper())
        elif i == "6":
            str1 += "."
        elif i == "7":
            str1 = str1.replace(str1[0], str1[0].upper(), 1)
        elif i == "8":
            str1 = str1[:: -1]
        else:
            str1 = "Invalid Input"
    print(str1)


usr_input = input("Enter ur Numbers: ")
list1 = list(usr_input)
GooglePassion(list1)
