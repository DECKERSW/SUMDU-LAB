import csv
import os

def convert_to_float(string_value):
    try:
        float_value = float(string_value)
        return float_value
    except ValueError:
        print("Неможливо конвертувати рядок у число")
        return None

try:
    with open("Lab11.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        print("Country Name: 2016 [YR2016]")
        for row in reader:
            print(row['Country Name'], ': ', row["2016 [YR2016]"])

except FileNotFoundError:
    print("Lab11.csv not found!")

try:
    with open("Lab11.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        indicator = float(input("\n Введіть будь-яке значення, щоб знайти показники, які більші, ніж значення, яке ви ввели: "))
        
        print(indicator)
        
        
        if indicator is not None:
            print("Country Name: 2016 [YR2016]")
            
            for row in reader:
                             
                if indicator < convert_to_float(row["2016 [YR2016]"]):
                    print(row["Country Name"], ": ", row["2016 [YR2016]"])
                    with open("new_lab11.csv", "a") as csvfile2:
                        writer = csv.writer(csvfile2, delimiter=";")
                        writer.writerow((row["Country Name"], row["2016 [YR2016]"]))

except FileNotFoundError:
    print("Lab11.csv not found!")
