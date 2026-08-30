import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 185.00
}


def show_available_stocks():
    print("\nAvailable Stocks:")
    print("-" * 30)

    for stock, price in stock_prices.items():
        print(f"{stock}: ${price:.2f}")


def save_portfolio(portfolio, total_value):
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Stock",
            "Quantity",
            "Price per Share",
            "Investment Value"
        ])

        for stock in portfolio:
            writer.writerow([
                stock["name"],
                stock["quantity"],
                stock["price"],
                stock["value"]
            ])

        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total_value])

    print("\nPortfolio successfully saved to portfolio.csv")


def main():

    portfolio = []
    total_value = 0

    print("=" * 45)
    print("        STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    show_available_stocks()

    while True:

        stock_name = input(
            "\nEnter stock symbol (or type 'done' to finish): "
        ).upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("Stock not available. Please choose from the list.")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        price = stock_prices[stock_name]

        investment_value = price * quantity

        portfolio.append({
            "name": stock_name,
            "quantity": quantity,
            "price": price,
            "value": investment_value
        })

        total_value += investment_value

        print(
            f"{stock_name} added successfully!"
        )

    print("\n" + "=" * 45)
    print("             YOUR PORTFOLIO")
    print("=" * 45)

    if not portfolio:
        print("No stocks were added.")
        return

    for stock in portfolio:

        print(
            f"{stock['name']} | "
            f"Quantity: {stock['quantity']} | "
            f"Price: ${stock['price']:.2f} | "
            f"Value: ${stock['value']:.2f}"
        )

    print("-" * 45)
    print(f"Total Investment Value: ${total_value:.2f}")
    print("=" * 45)

    save_choice = input(
        "\nWould you like to save the portfolio to CSV? (yes/no): "
    ).lower()

    if save_choice == "yes":
        save_portfolio(portfolio, total_value)
    else:
        print("Portfolio was not saved.")

    print("\nThank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()