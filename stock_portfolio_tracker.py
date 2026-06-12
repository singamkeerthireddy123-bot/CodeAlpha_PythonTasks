stocks = {"AAPL": 180, "TSLA": 250, "GOOG": 140}

total = 0
result = []

while True:
    stock = input("Enter stock name (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        qty = int(input("Enter quantity: "))
        value = stocks[stock] * qty
        total += value
        result.append(f"{stock} x {qty} = ${value}")
    else:
        print("Stock not found")

print("\nPortfolio Summary")
for i in result:
    print(i)

print("Total Investment: $", total)

with open("portfolio.txt", "w") as f:
    for i in result:
        f.write(i + "\n")
    f.write(f"Total Investment: ${total}")
