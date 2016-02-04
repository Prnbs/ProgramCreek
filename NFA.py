from RegEx import PostFix


class AST:
    pass


class Literal(AST):
    def __init__(self, lit):
        self.literal = lit


class Or(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Concat(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Repeat(AST):
    def __init__(self, expr):
        self.expr = expr


class Plus(AST):
    def __init__(self, expr):
        self.expr = expr


class State:
    pass


class Consume(State):
    def __init__(self, to_consume, out):
        self.to_consume = to_consume
        self.out = out


class Split(State):
    def __init__(self, out1, out2):
        self.out1 = out1
        self.out2 = out2


class Match(State):
    pass


class Placeholder(State):
    def __init__(self, pointing_to):
        self.pointing_to = pointing_to


class NFA:

    def postfix_2_AST(self, postfix_input):
        """
        Converts the input from post fix notation to an AST
        :param postfix_input:
        :return:
        """
        AST = []
        for ch in postfix_input:
            if ch is '*':
               expr = AST.pop()
               AST.append(Repeat(expr))
            elif ch is '+':
                expr = AST.pop()
                AST.append(Plus(expr))
            elif ch is '`':
                right = AST.pop()
                left = AST.pop()
                AST.append(Concat(left, right))
            elif ch is '|':
                right = AST.pop()
                left = AST.pop()
                AST.append(Or(left, right))
            else:
                AST.append(Literal(ch))

        return AST.pop()

    def AST_2_NFA(self, ast, and_then):
        """
        Converts the AST to an NFA
        :param ast:
        :param and_then:
        :return:
        """
        if isinstance(ast, Literal):
            return Consume(ast.literal, and_then)
        elif isinstance(ast, Concat):
            return self.AST_2_NFA(ast.left, self.AST_2_NFA(ast.right, and_then))
        elif isinstance(ast, Repeat):
            placeholder = Placeholder(None)
            split = Split(self.AST_2_NFA(ast.expr, placeholder), and_then)
            placeholder.pointing_to = split
            return placeholder
        elif isinstance(ast, Or):
            split = Split(self.AST_2_NFA(ast.left, and_then), self.AST_2_NFA(ast.right, and_then))
            return split
        elif isinstance(ast, Plus):
            return self.AST_2_NFA(Concat(ast.expr, Repeat(ast.expr)), and_then)
        else:
            return Consume("", and_then)

    def evaluate_NFA(self, curr_state, string_to_match):
        """
        Runs the string_to_match on the NFA to see if it can reach the Match state
        :param curr_state:
        :param string_to_match:
        :return:
        """
        if isinstance(curr_state, Consume):
            if len(string_to_match) == 0:
                return False
            if string_to_match[0] != curr_state.to_consume:
                return False
            return self.evaluate_NFA(curr_state.out, string_to_match[1:])
        elif isinstance(curr_state, Placeholder):
            return self.evaluate_NFA(curr_state.pointing_to, string_to_match)
        elif isinstance(curr_state, Split):
            lhs = self.evaluate_NFA(curr_state.out1, string_to_match)
            rhs = self.evaluate_NFA(curr_state.out2, string_to_match)
            return rhs | lhs
        elif isinstance(curr_state, Match):
            if len(string_to_match) > 0:
                return False
            else:
                return True


if __name__ == '__main__':
    obj = PostFix()
    input = "ab*"
    str = obj.append_concat(input[1:], input[0])
    postFix = obj.in2post(str)
    print("Postfixed", postFix)
    ndfa = NFA()
    nfa = ndfa.postfix_2_AST(postFix)
    state = ndfa.AST_2_NFA(nfa, Match())
    result = ndfa.evaluate_NFA(state, "abb")
    print(result)



