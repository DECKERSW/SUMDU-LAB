import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з CSV-файлу
data = pd.read_csv("OutOf.csv")

# Вивід перших декількох рядків для перевірки даних
print(data.head())

# Вибір даних для України та США
ukraine_data = data[data["Country Name"] == "Ukraine"]
usa_data = data[data["Country Name"] == "United States"]

# Вибір періоду
years = data.columns[4:]

# Побудова графіка на одній координатній осі
plt.figure(figsize=(10, 6))
plt.plot(years, ukraine_data.values.tolist()[0][4:], label="Україна")
plt.plot(years, usa_data.values.tolist()[0][4:], label="США")
plt.xlabel('Рік')
plt.ylabel('Значення показника')
plt.title('Динаміка показника для України та США')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()
