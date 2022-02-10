import csv
import operator


class Person_info:

    def __init__(self, data):
        self.data = data

    def sort_one(self):

        with open('dict.csv') as f:
            csv_reader = csv.reader(f, delimiter=';')
            print(sorted(csv_reader, key=operator.itemgetter(1)))

    def adding_line(self):
        with open('dict.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow((self.data['first_name'], self.data['last_name'], self.data['age'], self.data['gender'],
                             self.data['hobby'], self.data['job']))
            f.close()

    def update_line(self):

        row_num = 1
        new_value = 'Replaced Line'

        with open('dict.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter=';')
            lines = []

            for current_line in csv_reader:
                if csv_reader.line_num == row_num:
                    current_line = new_value
                lines.append(current_line)

        with open('dict.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(lines)

    def edit_line(self):
        line_to_editing = []
        with open('dict.csv') as f:
            csv_reader = csv.reader(f, delimiter=';')
            for row in csv_reader:
                line_to_editing.append(row)
        print(line_to_editing)


simple_person = {'first_name': 'Akbar', 'last_name': 'Maloer', 'age': 21, 'gender': 'male', 'hobby': 'PC',
         'job': 'Key_master'}
second_person = {'first_name': 'Moon', 'last_name': 'Troops', 'age': 23, 'gender': 'male', 'hobby': 'swimming',
         'job': 'BA'}


work = Person_info(simple_person)
work1 = Person_info(second_person)
work.adding_line()
work1.adding_line()
work.edit_line()
work.sort_one()
