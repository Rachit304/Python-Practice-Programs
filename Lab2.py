def Validate(C_Name, Qty, Stock, Status):
    space = " "
    if space in C_Name:
        return False

    if len(Status) > 2 or C_Name == "":
        return False

    if Stock <= 0 or Qty <= 0:
        return False

    if Status != 'b' and Status != 's':
        return False

    return True


print("----------Welcome to BSE----------")

broker = ""
small_list = big_list = []
tuple1 = ()
buy = sell = 0
while broker != 'I am gonna call tonight':

    c_name = input("Company Initials :- ")
    qty = int(input("Quantity of Stock:  "))
    stock = float(input("Value of Stock: "))
    status = input("Buy or Sell :- ")

    if Validate(c_name, qty, stock, status):
        small_list = [c_name, qty, stock, status]
        big_list.append(tuple(small_list))
        tuple1 = tuple(big_list)
    else:
        print("Invalid Input")

    broker = input("Do you want to call client or add stock  : ")


for i_tuple in tuple1:

    if i_tuple[3] == 'b':
        buy += i_tuple[1] * i_tuple[2]
    else:
        sell += i_tuple[1] * i_tuple[2]

print("buy: " + str(buy) + "   sell: " + str(sell))
