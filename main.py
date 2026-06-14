import tkinter as tk
from tkinter import messagebox, ttk
import storage
import logic

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Дневник производственной практики")
        self.root.geometry("500x600")

        #Поля ввода
        frame_input = tk.LabelFrame(root, text="Новая запись", padx=10, pady=10)
        frame_input.pack(padx=20, pady=10, fill="x")

        tk.Label(frame_input, text="Дата:").grid(row=0, column=0, sticky="w")
        self.entry_date = tk.Entry(frame_input)
        self.entry_date.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(frame_input, text="Что сделано:").grid(row=1, column=0, sticky="w")
        self.entry_work = tk.Entry(frame_input)
        self.entry_work.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(frame_input, text="Часы:").grid(row=2, column=0, sticky="w")
        self.entry_hours = tk.Entry(frame_input)
        self.entry_hours.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        btn_add = tk.Button(frame_input, text="Добавить запись", command=self.add_record, bg="lime")
        btn_add.grid(row=3, column=0, columnspan=2, pady=10)

        #Список записей
        frame_list = tk.LabelFrame(root, text="Записи в дневнике", padx=10, pady=10)
        frame_list.pack(padx=20, pady=10, fill="both", expand=True)

        self.listbox = tk.Listbox(frame_list, font=("Courier", 10))
        self.listbox.pack(fill="both", expand=True)

        #Кнопки
        frame_btns = tk.Frame(root, pady=20)
        frame_btns.pack()

        btn_del = tk.Button(frame_btns, text="Удалить выбранное", command=self.delete_record, bg="red")
        btn_del.pack(side="left", padx=10)

        btn_total = tk.Button(frame_btns, text="Посчитать часы", command=self.show_total)
        btn_total.pack(side="left", padx=10)

        #Обновляем список при запуске
        self.update_list()

    def update_list(self):
        self.listbox.delete(0, tk.END)
        formatted = logic.get_formatted_records()
        if formatted:
            for item in formatted:
                self.listbox.insert(tk.END, item)

    def add_record(self):
        date = self.entry_date.get().strip()
        work = self.entry_work.get().strip()
        hours_str = self.entry_hours.get().strip()

        if not date or not work or not hours_str:
            messagebox.showwarning("Ошибка", "Заполните все поля!")
            return

        try:
            hours = float(hours_str)
            if hours <= 0:
                raise ValueError("Часы должны быть больше нуля")
            
            storage.save_record(date, work, hours)
            messagebox.showinfo("Успех", "Запись добавлена!")
            
            # Очистка полей
            self.entry_work.delete(0, tk.END)
            self.entry_hours.delete(0, tk.END)
            self.update_list()
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Введите корректное число часов (больше 0)")

    def delete_record(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Внимание!", "Сначала выберите запись в списке!")
            return
        
        index = selected[0]
        success, message = logic.delete_record_by_index(index)
        
        if success:
            messagebox.showinfo("Удалено", f"Запись '{message}' удалена")
            self.update_list()
        else:
            messagebox.showerror("Ошибка", message)

    def show_total(self):
        total = logic.calculate_total_hours()
        messagebox.showinfo("Итог", f"Общее количество отработанных часов:\n{total} ч.")


root = tk.Tk()
app = DiaryApp(root)
root.mainloop()
