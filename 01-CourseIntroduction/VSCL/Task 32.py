amount = float(input("Amount paid:"))
vat_rate = 0.23
vat_amount = (amount * vat_rate)
formatted_amount = "{:.2f}".format(amount)
formatted_vat = "{:.2f}".format(vat_amount)
print(f"Amount paid: {formatted_amount}")
print(f"VAT 23%: {formatted_vat}")
