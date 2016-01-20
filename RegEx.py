
class PostFix:
    def __init__(self):
        self.rpn = []
        self.operator = []
        self.operators = {'+', '*', '-', '(', ')', '/', '^', '|'}
        self.binaryOperator = {'-', '/', '|'}
        self.unaryOperator ={'+', '*'}
        self.parenthesis = {'(', ')'}
        self.precedence = { '^': 4,
                            '*': 3,
                            '/': 3,
                            '+': 2,
                            '-': 2,
                            '(': 0,
                            ')': 0}

    def in2post(self, input):
        """
        Converts the in fixed input to post fix that is suitable to be used for reg ex matching.
        This is not a typical implementation as in a+b won't become ab+
        :param input:
        :return: A post fix string
        """
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
        """
        Decides the order in which to handle the operands when operators are present based on precedence
        :param input:
        :return:
        """
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

    def append_concat_recursive(self, input, result, num_operands, prev_operator=None):
        """
        Recursive function that decides where to put the . operator for concat
        :param input: at each recursive call the input size reduces by input[1:]
        :param result: at each recursive call result size increases by result += input[0]
        :param num_operands: number of operators seen so far, is equal to 1 then . will never be placed
        :param prev_operator: is prev_operator was a binary operator then . won't be placed
        :return:
        """
        if len(input) == 0:
            return result
        temp_result = result + input[0]
        head_is_operator = input[0] in self.operators
        head_is_bi_operator = input[0] in self.binaryOperator
        head_is_parenthesis = input[0] in self.parenthesis
        prev_operator_was_bi = prev_operator in self.binaryOperator
        if input[0].isalnum():
            num_operands += 1
        if num_operands > 1 and not head_is_bi_operator and head_is_operator and not head_is_parenthesis \
                and not prev_operator_was_bi:
            temp_result += '.'
        if head_is_operator:
            prev_operator = input[0]
        return self.append_concat_recursive(input[1:], temp_result, num_operands, prev_operator)

    def append_concat(self, input, result):
        """
        A landing function to call append_concat_recursive and set num_operands to 1 if needed
        :param input:
        :param result:
        :return:
        """
        num_operands = 0
        if result.isalnum():
            num_operands += 1
        return self.append_concat_recursive(input, result, num_operands)


if __name__ == '__main__':
    post_fix = PostFix()
    input = "a*b+"
    appended = post_fix.append_concat(input[1:], input[0])
    print(appended)
    print(post_fix.in2post(appended))