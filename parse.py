import csv

with open('/Repo/Capstone2-15/input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(f'{line_count} \t{row[0]} \t {row[1]}')
        line_count+=1