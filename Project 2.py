class Expense:
		
		def __init__(self, amount, category, description):
			self.amount = amount
			self.category = category
			self.description = description
		
		def display(self):
			print("-------------------")
			print(f"Amount : {self.amount}")
			print(f"Category : {self.category}")
			print(f"Description : {self.description}")
		
class Tracker:
		def __init__(self):
			self.__expenses = [ ]
			
		def add_expense(self,expense):
			self.__expenses.append(expense)
			
		def show_all(self):
			for ex in self.__expenses:
				ex.display()
				
		def total (self):
			total = 0
			for ex in self.__expenses:
				total += ex.amount
			return total 
			
		def show_by_category(self, category):
			for ex in self.__expenses:
				if ex.category == category:
					ex.display()
					
		def total_by_category(self, category):
			total = 0
			for ex in self.__expenses:
				if ex.category == category:
					total += ex.amount
			return total
			
		def summary(self):
			print("======= EXPENSE SUMMARY =======")
			print(f"Total Expenses : {len(self.__expenses)}")
			print(f"Total Money   : ₹{self.total()}")
			print("-------------------------------")
			categories = set()
			for ex in self.__expenses:				
				categories.add(ex.category)
				
			for cat in categories :
				print(f"{cat} : ₹{self.total_by_category(cat)}")
			print("===============================")
				

t = Tracker()

t.add_expense(Expense(1200, "Food", "Lunch at hotel"))
t.add_expense(Expense(1000, "Food", "Lunch at hotel"))
t.add_expense(Expense(500, "Transport", "Rickshaw"))
t.add_expense(Expense(2000, "Shopping", "New earphones"))

t.show_all()
t.summary()
