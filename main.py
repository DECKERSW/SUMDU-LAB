import csv
import json

def csv_to_json(csv_file, json_file):
    
    #Зчитує дані з .csv файлу та записує їх у .json файл.

    try:
        # Відкриття .csv файлу для читання
        with open(csv_file, 'r', newline='') as csvfile:
            # Читання даних з .csv файлу
            csv_reader = csv.DictReader(csvfile)
            # Конвертуємо дані у список словників
            data = [row for row in csv_reader]

        # Запис даних у .json файл
        with open(json_file, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        print(f'Data has been converted from {csv_file} to {json_file} successfully.')
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def main():
    csv_file = 'Start.csv'  # Початковий .csv файл
    json_file = 'output.json'  # Вихідний .json файл
    csv_to_json(csv_file, json_file)

if __name__ == "__main__":
    main()
