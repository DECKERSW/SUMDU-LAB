import json


countries = [
    {"name": "Ukraine", "population": 44000000, "area": 603700, "continent": "Europe"},
    {"name": "China", "population": 1400000000, "area": 9596960, "continent": "Asia"},
    {"name": "Nigeria", "population": 206000000, "area": 923768, "continent": "Africa"},
    {"name": "India", "population": 1380000000, "area": 3287260, "continent": "Asia"},
    {"name": "Egypt", "population": 104000000, "area": 1002450, "continent": "Africa"},
    {"name": "Japan", "population": 126000000, "area": 377975, "continent": "Asia"},
    {"name": "Brazil", "population": 213000000, "area": 8515767, "continent": "South America"},
    {"name": "Ethiopia", "population": 114000000, "area": 1104300, "continent": "Africa"},
    {"name": "Pakistan", "population": 220000000, "area": 881913, "continent": "Asia"},
    {"name": "USA", "population": 336000000, "area": 9800000, "continent": "North America"}
]


with open("countries.json", "w") as file:
    json.dump(countries, file, indent=4)

while True:
    print("Select an option:\n 1 - Add data\n 2 - View data\n 3 - Find countries in Africa or Asia\n 4 - Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        # Додавання нового запису
        with open("countries.json", "r+") as file:
            data = json.load(file)
            print("Add a country:")
            name = input("Name: ")
            population = int(input("Population: "))
            area = int(input("Area: "))
            continent = input("Continent: ")
            new_country = {"name": name, "population": population, "area": area, "continent": continent}
            data.append(new_country)
            file.seek(0)
            json.dump(data, file, indent=4)

    elif choice == "2":
        # Виведення вмісту JSON файлу
        with open("countries.json", "r") as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))

    elif choice == "3":
        # Пошук країн в Африці або Азії
        with open("countries.json", "r") as file:
            data = json.load(file)
            african_countries = [country["name"] for country in data if country["continent"] == "Africa"]
            asian_countries = [country["name"] for country in data if country["continent"] == "Asia"]
            if african_countries:
                print("Countries in Africa:", african_countries)
            if asian_countries:
                print("Countries in Asia:", asian_countries)

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please select a valid option.")
