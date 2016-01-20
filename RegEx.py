
class PostFix:
    def __init__(self):
        self.rpn = []
        self.operator = []
        self.operators = {'+', '*', '-', '(', ')', '/', '^'}
        self.unaryOperator ={'+', '*'}
        self.precedence = { '^': 4,
                            '*': 3,
                            '/': 3,
                            '+': 2,
                            '-': 2,
                            '(': 0,
                            ')': 0}

    def in2post(self, input):
        for ch in input:
            if ch.isalnum() or ch is '.':
                self.rpn.append(ch)
            elif ch in self.operators and ch not in self.unaryOperator:
                self.handle_operators(ch)
            else:
                self.rpn.append(ch)
        while len(self.operator) > 0:
            self.rpn.append(self.operator.pop())
        # self.rpn.reverse()
        return "".join(self.rpn)

    def handle_operators(self, input):
        if input is '(':
            # self.operator.append(input)
            pass
        elif input is ')':
            while len(self.operator) > 0 and self.operator[-1] is not '(':
                self.rpn.append(self.operator.pop())
            # self.operator.append(input)
        else:
            while len(self.operator) > 0 and (self.precedence[self.operator[-1]] >= self.precedence[input()]):
                self.rpn.append(self.operator.pop())
            self.operator.append(input)

    def append_concat(self, input, result):
        if len(input) == 0:
            return result
        temp_result = result + input[0]
        # terminating condition
        if len(input) == 1:
            return temp_result + "."

        if input[0] is '(':
            temp_result += input[1]
            temp_result = self.append_concat(input[2:input.find(')')], temp_result) + ')'
            temp_result = self.append_concat(input[input.find(')') + 1:], temp_result)
        else:
            if input[1] not in self.unaryOperator:
                temp_result += '.'
            temp_result = self.append_concat(input[1:], temp_result)
        return temp_result

if __name__ == '__main__':
    post_fix = PostFix()
    input = "ab(dd)*(de)+"
    appended = post_fix.append_concat(input[1:], input[0])
    print(appended)
    print(post_fix.in2post(appended))