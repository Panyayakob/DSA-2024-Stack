class Stack:
    def __init__(self):
        self.stack = []  

    def push(self, data):
        """เพิ่มข้อมูลเข้าไปใน stack"""
        self.stack.append(data)

    def pop(self):
        """ดึงข้อมูลออกจาก stack"""
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        """ตรวจสอบว่า stack ว่างหรือไม่"""
        return len(self.stack) == 0

def evaluate_postfix(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit(): 
            stack.push(int(token))
        else:  
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
           
                if operand2 != 0:
                    stack.push(operand1 / operand2)
                else:
                    return "Error: Division by zero"
    return stack.pop()

postfix_expression = input("Enter a Postfix expression: ")

result = evaluate_postfix(postfix_expression)

print("Result:", result)
