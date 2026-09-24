principle=float(input("enter the number"))
interest=float(input("enter the interest"))
time=float(input("enter time in year"))
simple_interest=(principle*interest*time)/100
total_amount=principle+simple_interest
print(f"your simple interest is = {simple_interest}")
print(f"your total amount is= {total_amount}")
