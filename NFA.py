from RegEx import PostFix

class RegExpr:
    pass


class Literal(RegExpr):
    def __init__(self, lit):
        self.literal = lit


class Or(RegExpr):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Concat(RegExpr):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Repeat(RegExpr):
    def __init__(self, expr):
        self.expr = expr


class Plus(RegExpr):
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
        AST = []
        for ch in postfix_input:
            if ch is '*':
               expr = AST.pop()
               AST.append(Repeat(expr))
            elif ch is '+':
                expr = AST.pop()
                AST.append(Plus(expr))
            elif ch is '.':
                if len(AST) >= 2:
                    right = AST.pop()
                    left = AST.pop()
                    AST.append(Concat(left, right))
                else:
                    left = AST.pop()
                    AST.append(Concat(left, ""))
            else:
                AST.append(Literal(ch))

        return AST.pop()

    def AST_2_NFA(self, ast, and_then):
        if isinstance(ast, Literal):
            return Consume(ast.literal, and_then)
        elif isinstance(ast, Concat):
            return self.AST_2_NFA(ast.left, self.AST_2_NFA(ast.right, and_then))
        elif isinstance(ast, Repeat):
            placeholder = Placeholder(None)
            split = Split(self.AST_2_NFA(ast.expr, placeholder), and_then)
            placeholder.pointing_to = split
            return placeholder
        elif isinstance(ast, Plus):
            return self.AST_2_NFA(Concat(ast.expr, Repeat(ast.expr)), and_then)
        else:
            # empty right side from concat
            return Consume("", and_then)

    def evaluate_NFA(self, curr_state, string_to_match):
        if isinstance(curr_state, Consume):
            if len(string_to_match) == 0:
                return True
            if string_to_match[0] != curr_state.to_consume:
                return False
            return self.evaluate_NFA(curr_state.out, string_to_match[1:])
        elif isinstance(curr_state, Placeholder):
            return self.evaluate_NFA(curr_state.pointing_to, string_to_match)
        elif isinstance(curr_state, Split):
            lhs = self.evaluate_NFA(curr_state.out1, string_to_match)
            rhs = lhs & self.evaluate_NFA(curr_state.out2, string_to_match)
            return rhs
        elif isinstance(curr_state, Match):
            return True


if __name__ == '__main__':
    obj = PostFix()
    input = "a*b+"
    str = obj.append_concat(input[1:], input[0])
    postFix = obj.in2post(str)
    print("Postfixed", postFix)
    ndfa = NFA()
    nfa = ndfa.postfix_2_AST("a*b.")
    state = ndfa.AST_2_NFA(nfa, Match())
    result = ndfa.evaluate_NFA(state, "aaaaaaaaab")
    print(result)



