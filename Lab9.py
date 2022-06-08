import zodiac

class InvalidFormat(Exception):
    pass
class quitException(Exception):
    message = "Program Terminated please try Again..."


def format(date):
    try:
        if len(date) != 10:
            raise InvalidFormat('Invalid Length Error : Strictly Enter the date in (dd/mm/yyyy) format...!')
            return False
        else:
            return True

        if date[2] != '/' or date[5] != '/':
            raise InvalidFormat('Format Error : Strictly Enter the date in (dd/mm/yyyy) format...!')
        else:
            return True

    except InvalidFormat as e:
        print(e)


def monthchk(date):
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:])

    isvalid = True

    list1 = [1, 3, 5, 7, 8, 10, 12]
    try:
        if month > 12:
            raise InvalidFormat('Out of Bound Error: Month Out of Bound !!')

        if month in list1:
            if day > 31:
                raise InvalidFormat('Out of Bound Error: Day Out of Bound !!')

        elif month == 2:
            if year % 4 == 0:
                if day > 29:
                    raise InvalidFormat('Out of Bound Error: Day Out of Bound !!')
            else:
                if day > 28:
                    raise InvalidFormat('Out of Bound Error: Day Out of Bound !!')
        else:
            if day > 30:
                raise InvalidFormat('Out of Bound Error: Day Out of Bound !!')
    except InvalidFormat as e:
        print(e)
        isvalid = False
    return isvalid



date = input("Enter Date:")
try:
    if date == "":
        print("Please Enter Any Date")
    elif date == '?':
        print("Pls !!! Enter Ur DOB...")
    elif date.lower() == 'q':
        raise quitException()
    else:
        if format(date):
           if monthchk(date):

               zodiac.zodiac()

except quitException as qe:
    print(qe.message)

