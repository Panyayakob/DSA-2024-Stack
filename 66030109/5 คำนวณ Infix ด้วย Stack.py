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
            return None

    def peek(self):
        """ดูข้อมูลที่อยู่บนสุดของ stack โดยไม่ดึงออก"""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        """ตรวจสอบว่า stack ว่างหรือไม่"""
        return len(self.stack) == 0
    
def precedence(op):
    """ฟังก์ชันตรวจสอบลำดับความสำคัญของตัวดำเนินการ"""
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def apply_operator(operand1, operand2, operator):
    """ฟังก์ชันสำหรับประมวลผลตัวดำเนินการ"""
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '/':
        if operand2 != 0:
            return operand1 / operand2
        else:
            raise ValueError("Error: Division by zero")
    if operator == '^':
        return operand1 ** operand2

def evaluate_infix(expression):
    operand_stack = Stack()  
    operator_stack = Stack()  

    i = 0
    while i < len(expression):
        char = expression[i]

        if char == ' ':
            i += 1
            continue

      
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            operand_stack.push(num)
            continue

       
        elif char in "+-*/^":
            while (not operator_stack.is_empty() and
                   precedence(operator_stack.peek()) >= precedence(char)):
                operator = operator_stack.pop()
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = apply_operator(operand1, operand2, operator)
                operand_stack.push(result)
            operator_stack.push(char)

       
        elif char == '(':
            operator_stack.push(char)

      
        elif char == ')':
            while operator_stack.peek() != '(':
                operator = operator_stack.pop()
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = apply_operator(operand1, operand2, operator)
                operand_stack.push(result)
            operator_stack.pop() 

        i += 1

  
    while not operator_stack.is_empty():
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        result = apply_operator(operand1, operand2, operator)
        operand_stack.push(result)

    return operand_stack.pop()


infix_expression = input("Enter an infix expression: ")

try:
    result = evaluate_infix(infix_expression)
    print("Result:", result)
except ValueError as e:
    print(e)
