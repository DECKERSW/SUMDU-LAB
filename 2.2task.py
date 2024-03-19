import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з CSV-файлу
data = pd.read_csv("OutOf.csv")
#Вивід перших та декількох останніх рядків для перевірки даних
print(data["Country Name"])

# Запитуємо користувача про назву країни
country_name = input("Введіть назву країни: ")

# Вибір даних для обраної країни
country_data = data[data["Country Name"] == country_name]

# Вибір періоду
years = data.columns[4:]

# Побудова стовпчатої діаграми
plt.figure(figsize=(8, 5))
plt.bar(years, country_data.values.tolist()[0][4:])
plt.xlabel('Рік')
plt.ylabel('Значення показника')
plt.title('Показник для {}'.format(country_name))
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

