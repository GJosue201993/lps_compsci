print("How much do the nachos cost?")
naco_price= int(raw_input())
print("How much money do you have in your pocket?") 
cash = int(raw_input())

if  nacho_price > cash: 
          print("Sorry no nachps for ypu!")
if nacho_price <= cash:
          print("Woot, nachos!")
if nacho_price == cash:
print("Thanks for using nacho_buyer.py")
