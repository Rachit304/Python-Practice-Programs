import OMG

print("-----------------Please Enter the Card Details-----------------")

cc_numbers = input("Enter the Card Number : ")
cvv = input("Enter The CVV : ")
exp_date = input("Enter The Expiry Date : ")
print("------------------------------------\n")

if OMG.ValidateCreditCard(cc_numbers):
    print("You Have Valid Card...Moving ahead for payment")
else:
    print("Transaction Failed..Not a valid card")
