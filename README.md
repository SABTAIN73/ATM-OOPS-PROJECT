# Python OOP ATM

A simple command-line ATM system built with Python using Object-Oriented Programming.

I made this project to practice Python OOP concepts while building something practical.

## Features

- PIN login with 3 attempts
- Check balance
- Deposit money
- Withdraw money
- Account details
- Transaction history
- Input validation
- Menu-driven interface
- Clears terminal screen

## OOP Concepts Used

- Classes and objects
- __init__() constructor
- self keyword
- Attributes
- Methods

## Python Concepts Used

- Variables
- Strings and integers
- Lists
- if, elif, else
- for and while loops
- Functions and methods
- input()
- Type conversion (int, str)
- String methods like isdigit()
- List append()
- import and modules

## How It Works

When the program starts, it creates an ATM object with some default account details.

The user has to enter the correct PIN to log in. They get 3 tries. If all 3 fail, the card gets blocked.

After login, the user sees a menu:

1. Check Balance
2. Deposit
3. Withdraw
4. Account Details
5. History
6. Exit

## Files

- python-oop-atm.py - the main program
- README.md - this file

## Requirements

- Python 3
- Only the os module from the standard library is used

## How to Run

Clone the repo:

    git clone https://github.com/SABTAIN73/ATM-OOPS-PROJECT.git

Go into the folder:

    cd ATM-OOPS-PROJECT

Run the program:

    python python-oop-atm.py

On some systems you may need to use python3 instead of python.

## Sample Run

    === ATM ===
    Enter PIN: 0789

    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Account Details
    5. History
    6. Exit
    Choose: 1
    Balance: 12000000000

## Notes

- The default PIN is 0789. You can change it in the code.
- Balance and PIN are stored as plain values since this is a learning project.
- No external libraries are needed.

## Author

Sabtain
GitHub: https://github.com/SABTAIN73
