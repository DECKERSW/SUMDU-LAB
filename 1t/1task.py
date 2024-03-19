import pandas as pd

# Створюємо словник з інформацією про країни
countries_info = {
    "Ukraine": {"Area": 603500, "Population": 41830000, "Continent": "Europe"},
    "Nigeria": {"Area": 923768, "Population": 206139587, "Continent": "Africa"},
    "China": {"Area": 9596961, "Population": 1444216107, "Continent": "Asia"},
    "Argentina": {"Area": 2780400, "Population": 45195777, "Continent": "South America"},
    "Australia": {"Area": 7692024, "Population": 25687041, "Continent": "Australia"},
    "Egypt": {"Area": 1002450, "Population": 104258327, "Continent": "Africa"},
    "India": {"Area": 3287263, "Population": 1393409038, "Continent": "Asia"},
    "Brazil": {"Area": 8515767, "Population": 213993437, "Continent": "South America"},
    "Kenya": {"Area": 580367, "Population": 53771296, "Continent": "Africa"},
    "Japan": {"Area": 377975, "Population": 126150000, "Continent": "Asia"},
}

# Перетворюємо словник у DataFrame
df = pd.DataFrame.from_dict(countries_info, orient='index')

# Виводимо DataFrame на екран
print("DataFrame з інформацією про країни:")
print(df)
print()

# Агрегація даних: обчислюємо загальну площу та населення за континентами
aggregated_data = df.groupby('Continent').agg({'Area': 'sum', 'Population': 'sum'})

# Виводимо агреговані дані на екран
print("Агреговані дані за континентами:")
print(aggregated_data)
