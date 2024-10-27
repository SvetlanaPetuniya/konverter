from tkinter import *
from tkinter import messagebox as mb
import requests
from tkinter import ttk


def exchange():
    code=combobox.get()

    if code:
        try:
            response=requests.get(f"https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data=response.json()

            if code in data ["rates"]:
                exchange_rate=data["rates"][code]
                mb.showinfo("Курс обмена", f"Курс к доллару: {exchange_rate:.1f}{code} за 1 доллар")
            else:
                mb.showerror("Ошибка", f"Валюта{code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка {e}")
    else:
        mb.showwarning("Внимание", "Введите код валюты")



window=Tk()
window.title("Конвертер валют")
window.geometry("400x500")


ttk.Label(text="Введите код валюты").pack(pady=10)

popular_cur=["EUR","JPY","GBP", "AUD","CAD", "CHF","CNY", "RUB","KZT","UZS"]
combobox=ttk.Combobox(values=popular_cur)
combobox.pack(pady=10)


ttk.Button(text="Получить курс обмена к доллару", command=exchange).pack(pady=10)

window.mainloop()
