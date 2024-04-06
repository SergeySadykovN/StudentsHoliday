import csv
import re


def write_holiday_cities(first_letter):
    travel_notes = []
    visited_set = set()
    wish_set = set()

    # Получить данные из travel_notes.csv & записать в holiday.csv
    with (open('travel-notes.csv', 'r', newline='', encoding='utf8') as file_read):
        reader = csv.reader(file_read)  # ридер для входного файла

        for row in reader:

            if row[0].startswith(first_letter):  # условие поиска по первой букве слова
                pattern = r"\w+(?:(?:[^;]*\[[^][]*])+[^;]*|[^;']+)"
                travel_notes.append(row)  # добавляем соответсвующие столбцы в список

                cities = re.findall(pattern, row[1])  # столбец с посещенными городами добавляем в список
                for city in cities:
                    visited_set.add(city)
                # print(visited_set)

                cities = re.findall(pattern, row[2])  # столбец с городами где не были добавляем в список
                for city in cities:
                    wish_set.add(city)
                # print(visit_set)

    all_cities = visited_set.union(wish_set)  # все города для всех имен
    not_been = (all_cities.difference(visited_set))  # где не были для всех имен
    next_city = sorted(not_been)[0] if not_been else ''  # следующий город

    # создаем файл для записи
    with (open('holiday.csv', 'w', newline='', encoding='utf8') as file_out):
        writer = csv.writer(file_out)  # врайтер для записи данных в holiday.csv

        writer.writerow(['Уже были в: ', ', '.join(sorted(visited_set))])
        writer.writerow(['Хотят побывать в: ', ', '.join(sorted(wish_set))])
        writer.writerow(['Еще не были в: ', ', '.join(not_been)])
        writer.writerow(['Следующий город: ', next_city])


letter = "L"
find_cities_by_letter_name = write_holiday_cities(letter)