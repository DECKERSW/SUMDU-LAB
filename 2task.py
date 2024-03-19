import pandas as pd
import matplotlib.pyplot as plt
# Завантаження даних з CSV файлу
df = pd.read_csv('comptage_velo_2018.csv', skipinitialspace=True, parse_dates=['Date'], dayfirst=True)
print(df)

# Виділення місяця з кожної дати
df['Month'] = df['Date'].dt.month

# Створення стовпця 'Total', що містить суму значень за кожен місяць
monthly_totals = df.iloc[:, 2:24].sum(axis=1)

# Групування за місяцем та обчислення суми для кожного місяця
monthly_summaries = monthly_totals.groupby(df['Month']).sum()

# Виведення результатів
for month, total in monthly_summaries.items():
    print(f"Месяц {month}: {total}")

# Знаходження місяця з найбільшою сумою
most_popular_month = monthly_summaries.idxmax()

# Виведення результатів
print("Найбільш популярний місяць у велосипедистів:", most_popular_month)

# Виведення всіх даних на одному графіку
plt.figure(figsize=(15,10))

# Побудова графіків для кожної колонки, за винятком колонки 'Date'
for column in df.columns:
    if column != 'Date':
        plt.plot(df['Date'], df[column], label=column)

# Налаштування осей та заголовка
plt.xlabel('Date')
plt.ylabel('Number of Cyclists')
plt.title('Bike Usage in 2018')
plt.legend()

# Поворот міток на осі x для кращої видимості
plt.xticks(rotation=45)

# Відображення графіка
plt.tight_layout()
plt.show()
