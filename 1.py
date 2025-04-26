import os

# Встановити директорію де знаходиться сам файл програми, для того щоб працювати з file.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Функція Денисенка Дениса для початку програми
def func1():
    try:
        # Введення даних
        pryzvishe = input("Введіть прізвище: ")
        pytanya = input("Введіть питання: ")

        # Відкриваємо файл з перезаписом всієї інформації
        with open("file.txt", "w", encoding="utf-8") as file:
            file.write(f"{pryzvishe}\n")
            file.write(f"{pytanya}\n\n")
        print("Файл успішно перезаписано")
    except IOError:
        print("Помилка: файлу file.txt не існує")

# Виклик функції Денисенка Дениса
func1()