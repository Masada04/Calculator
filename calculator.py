import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("เครื่องคิดเลข")
        self.window.geometry("400x600")
        self.window.configure(bg='#2C3E50')  # สีพื้นหลัง
        
        # สร้าง Style สำหรับปุ่ม
        style = ttk.Style()
        style.configure('Num.TButton', font=('Arial', 14), padding=10)
        style.configure('Op.TButton', font=('Arial', 14), padding=10)
        style.configure('Equal.TButton', font=('Arial', 14), padding=10)
        
        # หน้าจอแสดงผล
        display_frame = tk.Frame(self.window, bg='#2C3E50', pady=20)
        display_frame.pack(fill='x', padx=20)
        
        self.display = tk.Entry(
            display_frame,
            width=20,
            font=('Arial', 24),
            justify='right',
            bg='#ECF0F1',
            fg='#2C3E50',
            bd=10,
            relief='sunken'
        )
        self.display.pack(fill='x', padx=5)
        
        # สร้าง Frame สำหรับปุ่มกด
        button_frame = tk.Frame(self.window, bg='#2C3E50')
        button_frame.pack(padx=20, pady=20)
        
        # ปุ่มตัวเลขและเครื่องหมาย
        buttons = [
            ('C', 0, 0, 'Op.TButton', '#E74C3C'),
            ('(', 0, 1, 'Op.TButton', '#E67E22'),
            (')', 0, 2, 'Op.TButton', '#E67E22'),
            ('/', 0, 3, 'Op.TButton', '#E67E22'),
            ('7', 1, 0, 'Num.TButton', '#3498DB'),
            ('8', 1, 1, 'Num.TButton', '#3498DB'),
            ('9', 1, 2, 'Num.TButton', '#3498DB'),
            ('*', 1, 3, 'Op.TButton', '#E67E22'),
            ('4', 2, 0, 'Num.TButton', '#3498DB'),
            ('5', 2, 1, 'Num.TButton', '#3498DB'),
            ('6', 2, 2, 'Num.TButton', '#3498DB'),
            ('-', 2, 3, 'Op.TButton', '#E67E22'),
            ('1', 3, 0, 'Num.TButton', '#3498DB'),
            ('2', 3, 1, 'Num.TButton', '#3498DB'),
            ('3', 3, 2, 'Num.TButton', '#3498DB'),
            ('+', 3, 3, 'Op.TButton', '#E67E22'),
            ('0', 4, 0, 'Num.TButton', '#3498DB'),
            ('.', 4, 1, 'Num.TButton', '#3498DB'),
            ('=', 4, 2, 'Equal.TButton', '#27AE60'),
            ('⌫', 4, 3, 'Op.TButton', '#E74C3C')
        ]
        
        for (text, row, col, style_name, color) in buttons:
            cmd = lambda x=text: self.click(x)
            btn = ttk.Button(
                button_frame,
                text=text,
                command=cmd,
                style=style_name,
                width=5
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        
        # ทำให้ปุ่มยืดหยุ่นตามขนาดหน้าต่าง
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
            
    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == 'C':
            self.clear()
        elif key == '⌫':  # ปุ่มลบ
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])
        else:
            self.display.insert(tk.END, key)
            
    def clear(self):
        self.display.delete(0, tk.END)
        
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    calc = Calculator()
    calc.run()
