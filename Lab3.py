Morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
         'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----',
         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '......', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '"': '..-..-.',
         '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '/': '-..-.', '_': '..--.-',
         '=': '-...-', '+': '.-.-.', '-': '-....-', '$': '...-..-', '@': '.--.-.'}

choice = int(input("Choose Any  One :-\n1.)Normal String 2.) Morse String\n"))
if choice == 1:
    str1 = input("Enter Ur String :- ")
    str1 = str1.lower()
    space = " "
    if space not in str1:
        for i in str1:
            for key, value in Morse.items():
                if i == key:
                    print(value, end=" ")
    else:
        print("Only single word Accepted")

elif choice == 2:
    str1 = input("Enter Morse String :-")
    str1 = str1.split()
    for i in str1:
        for key, value in Morse.items():

            if i == value:
                print(key, end=" ")
else:
    str1 = ""
    print("Invalid Input")


