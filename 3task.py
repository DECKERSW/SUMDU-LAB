import json
import matplotlib.pyplot as plt

# Завантаження даних з файлу JSON
with open('countries.json') as f:
    data = json.load(f)

# Витягнення потрібних показників для кругової діаграми
countries = [country['name'] for country in data]
populations = [country['population'] for country in data]

# Обчислення відсоткових значень для населення
total_population = sum(populations)
percentages = [(population / total_population) * 100 for population in populations]

# Побудова кругової діаграми
plt.figure(figsize=(10, 10))
plt.pie(percentages, labels=countries, autopct='%1.1f%%')
plt.title('Population Distribution by Country')
plt.axis('equal')  # Забезпечує кругову форму діаграми
plt.show()

