# Stock Portfolio Tracker

## CodeAlpha Python Programming Internship

This project was developed as part of the **CodeAlpha Python Programming Internship**.

## Project Description

The Stock Portfolio Tracker is a simple Python application that allows users to enter stock symbols and quantities to calculate the total value of their investment portfolio.

Stock prices are stored in a predefined Python dictionary.

## Features

- Displays available stocks and their prices
- Allows users to enter stock symbols
- Accepts the quantity of shares
- Calculates investment value for each stock
- Calculates total portfolio value
- Validates invalid stock symbols
- Validates quantity input
- Displays a portfolio summary
- Saves portfolio information to a CSV file

## Available Stocks

The program contains predefined prices for:

- AAPL
- TSLA
- GOOGL
- MSFT
- AMZN

## Concepts Used

- Python dictionaries
- Lists
- Functions
- Loops
- Conditional statements
- User input/output
- Basic arithmetic
- Exception handling
- CSV file handling

## How to Run

Make sure Python is installed on your computer.

Open the project folder in a terminal and run:

```bash
python portfolio_tracker.py
```

Enter the stock symbol and quantity when prompted.

Type:

```text
done
```

when you have finished adding stocks.

The program will calculate and display the total portfolio value.

You can also choose to save the portfolio information to:

```text
portfolio.csv
```

## Example

```text
Enter stock symbol: AAPL
Enter quantity: 10

AAPL added successfully!

Enter stock symbol: MSFT
Enter quantity: 5

MSFT added successfully!

Enter stock symbol: done

YOUR PORTFOLIO

AAPL | Quantity: 10 | Price: $180.00 | Value: $1800.00
MSFT | Quantity: 5 | Price: $420.00 | Value: $2100.00

Total Investment Value: $3900.00
```

## Internship

This project is part of the Python Programming Internship offered by **CodeAlpha**.
