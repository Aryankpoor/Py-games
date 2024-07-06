MAX_LINES = 3


# Take user's bet before spinning the slot machine 
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
              break
            else:
                print("Amount must be greater than 0 ")
        else:
            print("Please enter a valid amount ")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" * str(MAX_LINES) + ")? ")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
              break
            else:
                print("Amount must be greater than 0 ")
        else:
            print("Please enter a valid amount ")
            
    return amount

def main():
     balance = deposit()
     
main()