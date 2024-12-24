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

    def is_empty(self):
        """ตรวจสอบว่า stack ว่างหรือไม่"""
        return len(self.stack) == 0


def reverse_string(input_string):
    stack = Stack()
    
    for char in input_string:
        stack.push(char)
    

    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

user_input = input("Enter a string: ")

reversed_result = reverse_string(user_input)

print("Reversed string:", reversed_result)
