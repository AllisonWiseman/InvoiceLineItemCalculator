#Allison Wiseman CIS261 Invoice Line Calculator

def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")
            
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. PLease try again.")
            
def main():
    print("The Invoice Line Item Calculator")
    
    while True:
        price = get_price()
        quantity = get_quantity()
        total = price * quantity
        
        print("\nPRICE:\t\t{:.2f}".format(price))
        print("QUANTITY:\t{}".format(quantity))
        print("TOTAL:\t\t{:.2f}\n".format(total))
        
        another = input("Enter another line item? (y/n): ").strip().lower()
        if another != 'y':
            break
        
    print("\nBye!")
    
if __name__ == "__main__":
    main()
    
