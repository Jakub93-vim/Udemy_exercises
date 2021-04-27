
import csv

data = open('Exercise_Files/find_the_link.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

link_list = []
for row_num,data in enumerate(data_lines):
    link_list.append(data[row_num])

''.join(link_list)