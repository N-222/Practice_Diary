import os

FILE_NAME = "diary.txt"

def save_record(date, work, hours):
    """Сохраняет одну запись в файл (в конец списка)"""
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        # Сохраняем данные через разделитель |, чтобы потом было легко разделить их обратно
        file.write(f"{date}|{work}|{hours}\n")

def load_all_records():
    """Загружает все записи из файла и возвращает их списком"""
    if not os.path.exists(FILE_NAME):
        return []
    
    records = []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                # Разделяем строку обратно на дату, работу и часы
                parts = line.split("|")
                records.append({
                    "date": parts[0], 
                    "work": parts[1], 
                    "hours": float(parts[2]) if parts[2] else 0.0
                })
    return records

def overwrite_file(records):
    """Полностью перезаписывает файл списком записей (нужно для удаления)"""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for rec in records:
            file.write(f"{rec['date']}|{rec['work']}|{rec['hours']}\n")

