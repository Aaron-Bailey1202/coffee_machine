# Coffee Machine Simulator

This is a simple Python program that simulates the functionality of a coffee machine. Users can choose from a selection of drinks, insert coins to pay for their order, and receive their drink along with any change due.

## Features

- **Drink Selection:** Users can choose from three different types of drinks: espresso, latte, and cappuccino.
- **Coin Insertion:** Users can insert coins of various denominations to pay for their order.
- **Resource Management:** The program tracks the resources required to make each drink, such as water, milk, and coffee beans, and checks if there are enough resources available before fulfilling an order.
- **Change Calculation:** If the user provides more money than required for their order, the program calculates and returns the appropriate change.
- **Reporting:** Users can request a report of the current status of the coffee machine, including the remaining resources and the amount of money collected.

## Usage

1. **Run the Program:** Execute the `coffee_machine.py` file using a Python interpreter.
2. **Follow On-Screen Prompts:** The program will prompt you to select a drink, insert coins, and provide your order. Follow the instructions provided.
3. **Shutdown:** To turn off the coffee machine, enter "off" when prompted for a drink choice.

## Dependencies

This program uses the `art` library to display ASCII art in the console. You can install it using pip:
