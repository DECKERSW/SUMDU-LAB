# Ім'я: Перший Студент
# Програма: Створення початкового файлу з питанням

def create_initial_file(file_name):
    try:
        with open(file_name, 'w') as file:
            # Записуємо прізвище першого студента та перше питання
            file.write("Last name: Kot\n")
            file.write("Question: How to display 'Hello, World!' in Python?\n")
        print(f"Файл {file_name} успішно створено з початковими даними.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

create_initial_file("questions.txt")
