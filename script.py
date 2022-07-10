#script para leer un archivo - https://www.codecademy.com/courses/learn-python-3/lessons/learn-python-files/exercises/reading-a-file

with open ('real_cool_document.txt') as cool_doc:
    cool_contents = cool_doc.read()
print(cool_contents)

with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)


with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
print(first_line)


#writing a file 'w'
#appending a file 'a'
#Usamos with con la identación para no tener que cerrar el archivo.

with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()
  print(setup)


#CSV
import csv
cool_facts = []
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row["Cool Fact"])

#generar csv
big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 
 
import csv
 
with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)
 
  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)