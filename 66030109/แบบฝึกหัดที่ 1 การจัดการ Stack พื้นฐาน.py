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

    def peek(self):
        """ดูข้อมูลที่อยู่บนสุดของ stack"""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def size(self):
        """ดูขนาดของ stack"""
        return len(self.stack)

stack = Stack()

for i in range(1, 6):
    data = input(f"Enter data for position {i}: ")
    stack.push(data)

print("Top of the stack:", stack.peek())

print("\nPopping 3 items from stack:")
for _ in range(3):
    popped_data = stack.pop()
    print(f"Popped: {popped_data}")

print("\nRemaining stack contents:", stack.stack)


