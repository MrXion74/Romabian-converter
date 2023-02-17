from roman import *
import tkinter as tk


def convert():
    num_str = entry_num.get()
    if var_conversion.get() == 'arabic to roman':
        if num_str.isnumeric():
            num = int(num_str)
            if num > 0 and num < 4000:
                result = arabic_to_roman(num)
                label_result.config(text=result)
            else:
                label_result.config(text='Ошибка: Число может быть от 1 до 3999')
        else:
            label_result.config(text='Ошибка: Неверный номер')
    elif var_conversion.get() == 'roman to arabic':
        try:
            result = roman_to_arabic(num_str)
            label_result.config(text=result)
        except ValueError:
            label_result.config(text='Ошибка: Неправильное Римское число')

root = tk.Tk()
root.title('Ромабиан конвертер')

label_num = tk.Label(root, text='Введите число:')
entry_num = tk.Entry(root)
label_conversion = tk.Label(root, text='Преобразование:')
var_conversion = tk.StringVar(value='arabic to roman')
radio_arabic_to_roman = tk.Radiobutton(root, text='Арабские в Римские', variable=var_conversion, value='arabic to roman')
radio_roman_to_arabic = tk.Radiobutton(root, text='Римские в Арабские', variable=var_conversion, value='roman to arabic')
button_convert = tk.Button(root, text='Конвертировать', command=convert)
label_result = tk.Label(root, text='', font=('Arial', 16), fg='red')

label_num.grid(row=0, column=0)
entry_num.grid(row=0, column=1)
label_conversion.grid(row=1, column=0)
radio_arabic_to_roman.grid(row=1, column=1)
radio_roman_to_arabic.grid(row=1, column=2)
button_convert.grid(row=2, column=1)
label_result.grid(row=3, column=1)

root.mainloop()