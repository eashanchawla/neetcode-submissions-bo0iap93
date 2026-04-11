class Solution:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def divide(self, a, b):
        return int(a / b)
    
    def multiply(self, a, b):
        return a * b

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': self.add, 
            '-': self.subtract, 
            '/': self.divide, 
            '*': self.multiply
        }
        stack = []
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                solution = operators[token](a, b)
                print(f'{a} {token} {b} = {solution}')
                stack.append(solution)
                print(stack)
            else:
                stack.append(int(token))
                print(stack)
        return stack.pop()
