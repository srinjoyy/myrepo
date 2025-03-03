x=5000
pin=int(input("Enter PIN: "))
new_pin=str(pin)
if len(new_pin)==4:
    print("""
          Press 1 to check balance
          Press 2 to withdraw
          Press 3 to deposit money""")
    n=int(input())
    if n==1:
        print(f"Balance is {x}")
    elif n==2:
        print("How much do you want to withdraw?")
        w=int(input())
        f=x-w
        if (f<0):
            print("Balance can't be negative")
        else:
            print(f"{w} is withdrawn. Balance is {f}")
    elif n==3:
        print("How much do you want to deposit?")
        y=int(input())
        g=x+y
        print(f"{g} is your new balance.")
    else:
        print("You've to select from the 3 options")
else:
    print("Enter proper pin number of 4 digits")