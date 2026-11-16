
import tkinter as tk
from tkinter import messagebox

# ساخت پنجره اصلی
root = tk.Tk()
root.title("اجتماعی هفتم - سازنده")
root.geometry("1000x625")
root.resizable(False, False)

# بارگذاری تصویر
try:
    img = tk.PhotoImage(file="image.png")
except Exception:
    messagebox.showerror(
        "خطا",
        "فایل image.png پیدا نشد!"
    )
    root.destroy()
    raise SystemExit

# نمایش تصویر
canvas = tk.Canvas(
    root,
    width=1000,
    height=625,
    highlightthickness=0
)
canvas.pack()

canvas.create_image(0, 0, image=img, anchor="nw")

# محدوده دکمه‌ها
buttons = [
    (16, 14, 283, 72, "گروه سه نام یک هدف"),

    (21, 267, 431, 360, "تست"),
    (438, 267, 856, 360, "گام به گام درس"),

    (21, 371, 431, 432, "هوش مصنوعی اجتماعی"),
    (438, 371, 856, 432, "صفحات کتاب"),

    (21, 441, 431, 502, "نکات"),
    (438, 441, 856, 502, "سوال و جواب"),

    (217, 512, 644, 563, "درباره"),

    # منوی سمت راست
    (867, 185, 999, 239, "خانه"),
    (867, 240, 999, 279, "کتابها"),
    (867, 280, 999, 320, "تست"),
    (867, 321, 999, 360, "صفحات کتاب"),
    (867, 361, 999, 403, "هوش مصنوعی اجتماعی"),
    (867, 404, 999, 447, "سوال و جواب"),
    (867, 448, 999, 493, "نکات"),
    (867, 505, 999, 554, "پیشرفت شما"),
]

# عملکرد کلیک دکمه‌ها
def click_button(event):
    x = event.x
    y = event.y

    for x1, y1, x2, y2, name in buttons:
        if x1 <= x <= x2 and y1 <= y <= y2:
            messagebox.showinfo(
                name,
                "این بخش هنوز فعال نشده است!"
            )
            return

# فعال کردن کلیک روی تصویر
canvas.bind("<Button-1>", click_button)

# اجرای برنامه
root.mainloop()
