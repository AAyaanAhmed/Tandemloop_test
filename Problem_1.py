class calculator:
    def __init__(self, a,b, op):
        self.a = float(a)
        self.b =float(b)
        self.op = op

    def calc(self):
        if self.op == '+':
            return self.a + self.b
        elif self.op == '-':
            return self.a - self.b
        elif self.op == '*':
            return self.a * self.b
        elif self.op == '/':
            return self.a / self.b
        else:
            return "Incorrect Input"


a = input("Enter first number: ")
b = input("Enter second number: ")
op = input("Enter operation(+, -,*,/): ")

output = calculator(a, b, op)
result = output.calc()
print("Result:", result)

