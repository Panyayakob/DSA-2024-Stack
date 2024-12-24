class Stack:
    def __init__(self):
        self.stack = []  # ใช้ list เป็นตัวแทนของ stack

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

# ฟังก์ชันแปลงจากฐาน 10 ไปเป็นฐาน 2
def decimal_to_binary(decimal):
    stack = Stack()
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        stack.push(str(decimal % 2))  # หารด้วย 2 และเก็บเศษ
        decimal = decimal // 2  # แบ่งตัวเลขด้วย 2
    
    binary = ''
    while not stack.is_empty():
        binary += stack.pop()  # ดึงตัวเลขจาก stack เพื่อสร้างผลลัพธ์ฐาน 2
    
    return binary

# ฟังก์ชันแปลงจากฐาน 10 ไปเป็นฐาน 16
def decimal_to_hexadecimal(decimal):
    stack = Stack()
    hex_digits = "0123456789ABCDEF"
    
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        stack.push(hex_digits[decimal % 16])  # หารด้วย 16 และเก็บเศษเป็นอักขระ
        decimal = decimal // 16  # แบ่งตัวเลขด้วย 16
    
    hexadecimal = ''
    while not stack.is_empty():
        hexadecimal += stack.pop()  # ดึงตัวเลขจาก stack เพื่อสร้างผลลัพธ์ฐาน 16
    
    return hexadecimal

# รับค่าจากผู้ใช้
decimal_number = int(input("Enter a decimal number: "))

# แปลงเป็นฐาน 2 และ ฐาน 16
binary_result = decimal_to_binary(decimal_number)
hexadecimal_result = decimal_to_hexadecimal(decimal_number)

# แสดงผลลัพธ์
print(f"Binary: {binary_result}")
print(f"Hexadecimal: {hexadecimal_result}")
