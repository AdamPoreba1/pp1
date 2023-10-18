product_price = float(input("Enter price: "))
discount_percentage = float(input("Enter discount %: "))
discount = (discount_percentage / 100) * product_price
discounted_price = product_price - discount
reduction = round(discount, 2)
print("Price with discount: {:.2f}".format(discounted_price))
print("Reduction: {:.2f}".format(reduction))