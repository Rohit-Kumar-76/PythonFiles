# Base class for showing welcome message
class CalculatorBase:
    def show_welcome(self):
        print("\n========== HYBRID CALCULATOR ==========")

# Class for basic operations (Addition, Subtraction)
class BasicOperations(CalculatorBase):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# Class for advanced operations (Multiplication, Division)
class AdvancedOperations(CalculatorBase):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

# Hybrid class
class Calculator(BasicOperations, AdvancedOperations):
    def menu(self):
        while True:
            self.show_welcome()
            print("""
Select Operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
""")
            choice = input("Enter your choice (1-5): ")

            if choice == '5':
                print("Thank you for using Hybrid Calculator! 👋")
                break

            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"Result: {a} + {b} = {self.add(a, b)}")
            elif choice == '2':
                print(f"Result: {a} - {b} = {self.subtract(a, b)}")
            elif choice == '3':
                print(f"Result: {a} * {b} = {self.multiply(a, b)}")
            elif choice == '4':
                print(f"Result: {a} / {b} = {self.divide(a, b)}")
            else:
                print("❌ Invalid choice. Please select between 1 to 5.")

# Run the calculator
calc = Calculator()
calc.menu()
