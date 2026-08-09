import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int (a / b)
        }
        for token in tokens:
            if token in operations:
                val_1 = stack.pop()
                val_2 = stack.pop()
                rs = operations[token](val_2, val_1)
                stack.append(rs)
            else:
                stack.append(int(token))
        return stack.pop()