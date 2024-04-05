import csv


def write_holiday_cities(first_letter):


    # Получить данные из travel_notes.csv & записать в holiday.csv
    with open('travel-notes.csv', 'r', newline='', encoding='utf8') as file_read, open('holiday.csv', 'w', encoding='utf8') as file_out:
        # создаем ридер для входного файла
        reader = csv.reader(file_read)

        # записываем данные в holiday.csv
        writer = csv.writer(file_out)

        for row in reader:
            been_list =[]
            if row[0].startswith(first_letter):
                been_list.append(row[1])
                print(been_list)



letter = "L"
write = write_holiday_cities(letter)
