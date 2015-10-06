__author__ = 'psinha4'

class RPN:
    def __init__(self):
        self.stack = []
        self.operators = ["+", "-", "/", "*"]

    def evalRPN(self, str_input):
        for i, char in enumerate(str_input):
              if char in self.operators:
                  right = self.stack.pop()
                  left  = self.stack.pop()
                  self.stack.append(self.handle_binary_operations(char, left, right))
              else:
                  self.stack.append(int(char))

        return self.stack.pop()

    def handle_binary_operations(self, operation, left, right):
        switcher = {
            "+" : self.plus,
            "-" : self.minus,
            "/" : self. divide,
            "*" : self.multiply
        }
        func = switcher.get(operation, lambda: "nothing")
        return func(left, right)

    def plus(self, left, right):
        return left + right

    def minus(self, left, right):
        return left - right

    def divide(self, left, right):
        if right != 0:
            return left / right
        else:
            return "NaN"

    def multiply(self, left, right):
        return left * right

if __name__ == "__main__":
    s_operation = ["22", "3","+", "2", "*"]
    rpn = RPN()
    print(rpn.evalRPN(s_operation))
