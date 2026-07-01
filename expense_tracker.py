import datetime as dt


class Expense:

    def __init__(self, amount, category, description):
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = dt.datetime.now().date()

    def display(self):
        print("----------------------------")
        print(f"Amount      : ₹{self.amount}")
        print(f"Category    : {self.category}")
        print(f"Description : {self.description}")
        print(f"Date        : {self.date}")


class Tracker:

    def __init__(self):
        self.__expenses = []

    def add_expense(self, expense):
        self.__expenses.append(expense)

    def show_all(self):
        if not self.__expenses:
            print("No expenses available.")
            return

        for ex in self.__expenses:
            ex.display()

    def total(self):
        total = 0
        for ex in self.__expenses:
            total += ex.amount
        return total

    def show_by_category(self, category):
        found = False

        for ex in self.__expenses:
            if ex.category.lower() == category.lower():
                ex.display()
                found = True

        if not found:
            print("No expenses found in this category.")

    def total_by_category(self, category):
        total = 0

        for ex in self.__expenses:
            if ex.category.lower() == category.lower():
                total += ex.amount

        return total

    def summary(self):

        if not self.__expenses:
            print("No expenses available.")
            return

        print("\n======= EXPENSE SUMMARY =======")
        print(f"Total Expenses : {len(self.__expenses)}")
        print(f"Total Amount   : ₹{self.total()}")
        print("-------------------------------")

        categories = set()

        for ex in self.__expenses:
            categories.add(ex.category)

        for cat in sorted(categories):
            print(f"{cat:<12} : ₹{self.total_by_category(cat)}")

        print("===============================\n")

    def save_to_file(self):

        with open("expenses.txt", "w") as f:
            for ex in self.__expenses:
                f.write(f"{ex.description}|{ex.category}|{ex.amount}|{ex.date}\n")

        print("Expenses saved successfully!")

    def load_from_file(self):

        try:
            with open("expenses.txt", "r") as f:

                self.__expenses.clear()

                for line in f:
                    line = line.strip()

                    if not line:
                        continue

                    parts = line.split("|")

                    if len(parts) != 4:
                        continue

                    description = parts[0]
                    category = parts[1]
                    amount = float(parts[2])
                    date = parts[3]

                    expense = Expense(amount, category, description)
                    expense.date = dt.datetime.strptime(
                        date, "%Y-%m-%d"
                    ).date()

                    self.__expenses.append(expense)

            print("Expenses loaded successfully!")

        except FileNotFoundError:
            print("No saved expenses found.")


def main():

    t = Tracker()

    t.add_expense(Expense(1200, "Food", "Lunch at hotel"))
    t.add_expense(Expense(500, "Transport", "Rickshaw"))
    t.add_expense(Expense(250, "Food", "Snacks"))
    t.add_expense(Expense(2000, "Shopping", "Headphones"))

    print("\nAll Expenses\n")
    t.show_all()

    print()
    t.summary()

    t.save_to_file()

    print("\nContents of expenses.txt\n")

    with open("expenses.txt", "r") as f:
        print(f.read())

    print("Loading data into new tracker...\n")

    t2 = Tracker()
    t2.load_from_file()

    t2.show_all()

    print()
    t2.summary()


if __name__ == "__main__":
    main()