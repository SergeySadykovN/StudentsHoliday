import csv
import re

travel_notes = []


def write_holiday_cities(first_letter):
    visited_set = set()
    visit_set = set()
    visited_dict = {}
    visit_dict = {}
    # Получить данные из travel_notes.csv & записать в holiday.csv
    with open('travel-notes.csv', 'r', newline='', encoding='utf8') as file_read, open('holiday.csv', 'w',
                                                                                       encoding='utf8') as file_out:
        # создаем ридер для входного файла
        reader = csv.reader(file_read)

        # записываем данные в holiday.csv
        writer = csv.writer(file_out)

        for row in reader:

            if row[0].startswith(first_letter):
                pattern = r"\w+(?:(?:[^;]*\[[^][]*])+[^;]*|[^;']+)"
                travel_notes.append(row)

                cities = re.findall(pattern, row[1])
                for city in cities:
                    visited_set.add(city)
                visited_dict[row[0]] = cities

                cities = re.findall(pattern, row[2])
                for city in cities:
                    visit_set.add(city)
                visit_dict[row[0]] = cities

        print(visited_dict)
        print(visit_dict)


letter = "A"
write = write_holiday_cities(letter)
