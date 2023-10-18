buys_euro = float(input("Bank buys EUR:"))
sells_euro = float(input("Bank sells EUR:"))
spread = (sells_euro) - (buys_euro)
spread_decimal = "{:.4f}".format(spread)
print(f"Spread: {spread_decimal}")

