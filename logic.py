from storage import load_all_records, overwrite_file

def calculate_total_hours():
    """Считает общую сумму часов по всем записям"""
    records = load_all_records()
    total = sum(rec['hours'] for rec in records)
    return total

def delete_record_by_index(index):
    """Удаляет запись по её номеру в списке"""
    records = load_all_records()
    
    # Проверка: существует ли такая запись (индекс не должен быть меньше 0 или больше длины списка)
    if 0 <= index < len(records):
        deleted_item = records.pop(index) # Удаляем элемент из списка
        overwrite_file(records)           # Перезаписываем файл обновленным списком
        return True, deleted_item['work']  # Возвращаем успех и название удаленной работы
    else:
        return False, "Запись с таким номером не найдена"

def get_formatted_records():
    """Возвращает список записей в красивом виде для вывода на экран"""
    records = load_all_records()
    if not records:
        return None
    
    # Формируем список строк: "12.05.2024 - Программирование (8ч)"
    formatted = []
    for i, rec in enumerate(records):
        line = f"{i}. {rec['date']} - {rec['work']} ({rec['hours']} ч.)"
        formatted.append(line)
    return formatted
