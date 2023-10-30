import tkinter as tk

# تابع محاسبه و نمایش نتایج
def calculate():
    # گرفتن مقادیر ورودی از ورودی‌ها
    price_usd_current = float(entry_price_usd.get())
    inflation_iran_current = float(entry_inflation_iran.get())
    inflation_usd_current = float(entry_inflation_usd.get())

    # محاسبه تقسیم نرخ تورم امریکا به نرخ تورم ایران
    inflation_ratio = (inflation_iran_current - inflation_usd_current )

    # محاسبه درصد تفاوت نرخ دلار
    percentage_difference = (inflation_ratio / 100)

    # محاسبه قیمت دلار واقعی
    real_usd_price1 = price_usd_current * percentage_difference
    real_usd_price = real_usd_price1 + price_usd_current

    # نمایش نتایج در فیلدهای مخصوص
    result_label.config(text=f"قیمت واقعی دلار در سال جاری: {real_usd_price:.2f}")

# تابع خروج از برنامه
def exit_app():
    root.destroy()

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("محاسبه قیمت دلار واقعی")

# تنظیم ابعاد کادر
root.geometry("350x150")

# ایجاد ورودی‌ها و بخش‌های مخصوص برای ورودی‌ها
entry_price_usd_label = tk.Label(root, text="قیمت فعلی دلار امریکا:")
entry_inflation_iran_label = tk.Label(root, text="نرخ تورم فعلی ایران:")
entry_inflation_usd_label = tk.Label(root, text="نرخ تورم فعلی امریکا:")
entry_price_usd = tk.Entry(root)
entry_inflation_iran = tk.Entry(root)
entry_inflation_usd = tk.Entry(root)

# ایجاد دکمه محاسبه با رنگ سبز
calculate_button = tk.Button(root, text="محاسبه", command=calculate, bg="green", fg="white")

# ایجاد دکمه خروج با رنگ قرمز
exit_button = tk.Button(root, text="خروج", command=exit_app, bg="red", fg="white")

# ایجاد بخش برای نمایش نتایج
result_label = tk.Label(root, text="")

# قرار دادن ورودی‌ها، بخش‌ها، و دکمه‌ها در پنجره با grid
entry_price_usd_label.grid(row=0, column=0)
entry_inflation_iran_label.grid(row=1, column=0)
entry_inflation_usd_label.grid(row=2, column=0)
entry_price_usd.grid(row=0, column=1)
entry_inflation_iran.grid(row=1, column=1)
entry_inflation_usd.grid(row=2, column=1)
calculate_button.grid(row=3, column=0, columnspan=2)
exit_button.grid(row=3, column=2, columnspan=2)
result_label.grid(row=4, column=0, columnspan=4)

# شروع نمایش پنجره
root.mainloop()
