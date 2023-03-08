card_number = input("Enter your card number : ")
if len(card_number) > 15:
    pass
else:
     print("Error") 


card_date = input("Enter your card date : ")
x = "/"
if x in card_date:
   pass
else:
    print("Error")


card_cvv = input("Enter your card cvv : ")
if len(card_cvv) == 3:
    pass
else:
    print("Error")
