import os  # used to clear the screen


class ATM:

    def __init__(self):
        # basic account info
        self.name = "sabtian"
        self.balance = 12000000000
        self.pin = "0789"
        self.history = []

    def login(self):
        # 3 attempts for PIN
        for i in range(3):
            user_pin = input("Enter PIN: ")

            if user_pin == self.pin:
                return True

            print("Wrong PIN")

        print("Card blocked")
        return False

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self):
        amount = input("Enter amount: ")

        if not amount.isdigit():
            print("Enter numbers only")
            return

        amount = int(amount)

        if amount <= 0:
            print("Amount must be more than 0")
            return

        self.balance = self.balance + amount
        self.history.append("Deposit: " + str(amount))

        print("Deposited:", amount)
        print("New balance:", self.balance)

    def withdraw(self):
        amount = input("Enter amount: ")

        if not amount.isdigit():
            print("Enter numbers only")
            return

        amount = int(amount)

        if amount <= 0:
            print("Amount must be more than 0")
            return

        if amount > self.balance:
            print("Not enough balance")
            return

        self.balance = self.balance - amount
        self.history.append("Withdraw: " + str(amount))

        print("Take your cash:", amount)
        print("New balance:", self.balance)

    def show_details(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

    def show_history(self):
        if len(self.history) == 0:
            print("No transactions yet")
        else:
            for item in self.history:
                print(item)

    def run(self):
        # clear screen before starting
        os.system("cls" if os.name == "nt" else "clear")

        print("=== ATM ===")

        if not self.login():
            return

        while True:
            print()
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Account Details")
            print("5. History")
            print("6. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                self.show_details()

            elif choice == "5":
                self.show_history()

            elif choice == "6":
                print("Thank you")
                break

            else:
                print("Wrong choice")


# create ATM object and start program
atm = ATM()
atm.run()