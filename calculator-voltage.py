def calculate_voltage(current, resistance):
    try:
        # คำนวณแรงดันไฟฟ้า
        voltage = current * resistance
        return voltage
    except Exception as e:
        return f"Error: {e}"

# ตัวอย่างการใช้งาน
# กระแสไฟฟ้า (I) ในหน่วยแอมแปร์
current = float(input("กรุณาใส่ค่ากระแสไฟฟ้า (I) ในหน่วยแอมแปร์: "))

# ความต้านทานไฟฟ้า (R) ในหน่วยโอห์ม
resistance = float(input("กรุณาใส่ค่าความต้านทานไฟฟ้า (R) ในหน่วยโอห์ม: "))

# เรียกใช้ฟังก์ชัน
voltage = calculate_voltage(current, resistance)

# แสดงผล
print(f"แรงดันไฟฟ้า (V) ที่คำนวณได้คือ: {voltage} โวลต์")
