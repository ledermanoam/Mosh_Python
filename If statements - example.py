
home_price = 1000
discount_price = (home_price-(0.10*home_price))
Buyer_credit = True

if Buyer_credit:
    new_price = discount_price
else:
    new_price = (home_price + (0.10*home_price))
print("the price is :" + str(new_price))