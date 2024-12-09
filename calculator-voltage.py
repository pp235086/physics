mport tkinter as tk
from tkinter import messagebox

def calculate_voltage():
    """
    ฟังก์ชันสำหรับคำนวณแรงดันไฟฟ้า (V) จากกระแสไฟฟ้า (I) และความต้านทาน (R)
    """
    try:
        # ดึงค่ากระแสไฟฟ้าและความต้านทานจากอินพุต
        current = float(entry_current.get())
        resistance = float(entry_resistance.get())
        
        # คำนวณแรงดันไฟฟ้า
        voltage = current * resistance
        
        # แสดงผลลัพธ์
        label_result.config(text=f"แรงดันไฟฟ้า (V): {voltage:.2f} โวลต์")
    except ValueError:
        # แสดงข้อความข้อผิดพลาดหากป้อนข้อมูลไม่ถูกต้อง
        messagebox.showerror("ข้อผิดพลาด", "กรุณาป้อนค่าตัวเลขที่ถูกต้อง!")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("แอปพลิเคชันคำนวณแรงดันไฟฟ้า")
root.geometry("400x300")  # กำหนดขนาดหน้าต่าง

# ส่วนหัวเรื่อง
label_header = tk.Label(root, text="โปรแกรมคำนวณแรงดันไฟฟ้า", font=("Helvetica", 16))
label_header.pack(pady=10)

# ส่วนอินพุต: กระแสไฟฟ้า
label_current = tk.Label(root, text="กระแสไฟฟ้า (I) หน่วยแอมแปร์:", font=("Helvetica", 12))
label_current.pack(pady=5)
entry_current = tk.Entry(root, font=("Helvetica", 12))
entry_current.pack(pady=5)

# ส่วนอินพุต: ความต้านทาน
label_resistance = tk.Label(root, text="ความต้านทาน (R) หน่วยโอห์ม:", font=("Helvetica", 12))
label_resistance.pack(pady=5)
entry_resistance = tk.Entry(root, font=("Helvetica", 12))
entry_resistance.pack(pady=5)

# ปุ่มคำนวณ
button_calculate = tk.Button(root, text="คำนวณ", command=calculate_voltage, font=("Helvetica", 12), bg="#4CAF50", fg="white")
button_calculate.pack(pady=15)

# ส่วนแสดงผลลัพธ์
label_result = tk.Label(root, text="แรงดันไฟฟ้า (V): ", font=("Helvetica", 12), fg="blue")
label_result.pack(pady=10)

# เริ่มต้นโปรแกรม
root.mainloop()
