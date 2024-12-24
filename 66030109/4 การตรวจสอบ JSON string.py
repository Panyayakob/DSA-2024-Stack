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

def is_valid_json(json_str):
    stack = Stack()
    
    open_brackets = {'{', '[', '('}
    close_brackets = {'}': '{', ']': '[', ')': '('}

    for char in json_str:
        if char in open_brackets:  
            stack.push(char)
        elif char in close_brackets: 
            if stack.is_empty() or stack.pop() != close_brackets[char]:
                return False  
    return stack.is_empty() 

json_string = input("Enter a JSON string: ")

if is_valid_json(json_string):
    print("The JSON string is valid.")
else:
    print("The JSON string is invalid.")
