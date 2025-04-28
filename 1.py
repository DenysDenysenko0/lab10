import os

# Встановити директорію де знаходиться сам файл програми, для того щоб працювати з file.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Функція для відкриття файлів
def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding='utf-8')
    except:
        print(f"Файл {file_name} не вдалося відкрити")
        return None
    else:
        print(f"Файл {file_name} успішно відкрито")
        return file

filename = "file.txt"

# Код Денисенка Дениса
file1 = Open(filename, "w") # "w" - відкриває файл для запису, перезаписуючи існуючий вміст.

if file1:
    # Введення даних
    pryzvishe = input("Введіть прізвище (№1): ")
    pytanya = input("Введіть питання: ")

    # Запис даних
    file1.write(f"{pryzvishe}\n")
    file1.write(f"{pytanya}\n\n")

    print("Текстовий файл успішно змінено")
    file1.close()

# Код Кубуші Олексія
file1 = Open(filename, "a") # "a" - відкриває файл для додавання нових даних в кінець файлу, не змінюючи існуючий вміст.

if file1:
    # Введення даних
    pryzvishe = input("Введіть прізвище (№2): ")
    vidpovid = input("Введіть відповідь на питання: ")
    pytanya = input("Введіть питання: ")

    # Запис даних
    file1.write(f"{pryzvishe}\n")
    file1.write(f"{vidpovid}\n")
    file1.write(f"{pytanya}\n\n")

    print("Текстовий файл успішно змінено")
    file1.close()