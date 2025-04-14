#from tkinter import *
#pro = Tk()
#pro.geometry('1000x900+300+50')
#pro.resizable( , True )
#pro.title('Newton Raphson')
#pro.config(background='black')
#root.iconbitmap('C:\\Users\\LORD\\Desktop\\ChatGPT Image Apr 13, 2025, 01_24_28 PM.png')

#pro.mainloop()





import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from tkinter import messagebox
import sympy as sp

# إنشاء النافذة
root = tk.Tk()
root.title("NEWTON RAPHSON METHOD")
root.geometry('1000x500+300+100')
#root.geometry("500x400")
root.resizable( False , False )
style = Style("morph")

# مدخلات المستخدم
label_func = tk.Label(root, text="Enter f(x):", font=("Cairo", 12))
label_func.pack(pady=5)
entry_func = tk.Entry(root, width=30, font=("Cairo", 12))
entry_func.pack(pady=20)

label_guess = tk.Label(root, text="Enter initial value (x₀):", font=("Cairo", 12))
label_guess.pack(pady=5)
entry_guess = tk.Entry(root, width=30, font=("Cairo", 12))
entry_guess.pack(pady=20)

label_iters = tk.Label(root, text="Enter the number of iterations:", font=("Cairo", 12))
label_iters.pack(pady=5)
entry_iters = tk.Entry(root, width=30, font=("Cairo", 12))
entry_iters.pack(pady=20)

output_label = tk.Label(root, text="", font=("Cairo", 12), wraplength=450)
output_label.pack(pady=20)

def newton_raphson():
    try:
        x = sp.Symbol('x')
        func_str = entry_func.get()
        func = sp.sympify(func_str)
        f_prime = sp.diff(func, x)
        
        x0 = float(entry_guess.get())
        n = int(entry_iters.get())
        
        for i in range(n):
            f_val = func.evalf(subs={x: x0})
            f_prime_val = f_prime.evalf(subs={x: x0})
            if f_prime_val == 0:
                raise ZeroDivisionError("Derivative = 0و cannot be divided by zero")
            x1 = x0 - f_val / f_prime_val
            x0 = x1

        output_label.config(text=f"The approximate solution after {n} iterations is:\n x ≈ {x0:.6f}")

    except Exception as e:
        messagebox.showerror("Error", f"error was happened:\n{str(e)}")

# زر التنفيذ
btn = tk.Button(root, text="Calculate", command=newton_raphson, font=("Cairo", 12, "bold"), bg="#3498db", fg="white", padx=10)
btn.pack(pady=10)

# تشغيل التطبيق
root.mainloop()