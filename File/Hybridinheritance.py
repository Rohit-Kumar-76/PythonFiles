# Base class for displaying a welcome message
class CalculatorBase:
    def show_welcome(self):
        print("Welcome to Hybrid Inheritance Calculator!\n")

# Class A (Addition, Subtraction) inherits from CalculatorBase
class BasicOperations(CalculatorBase):
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

# Class B (Multiplication, Division) inherits from CalculatorBase
class AdvancedOperations(CalculatorBase):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

# Final class inherits from both A and B → Hybrid Inheritance
class Calculator(BasicOperations, AdvancedOperations):
    def calculate(self, a, b):
        self.show_welcome()
        print(f"{a} + {b} = {self.add(a, b)}")
        print(f"{a} - {b} = {self.subtract(a, b)}")
        print(f"{a} * {b} = {self.multiply(a, b)}")
        print(f"{a} / {b} = {self.divide(a, b)}")

# Create object and perform operations
calc = Calculator()
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
calc.calculate(x, y)
