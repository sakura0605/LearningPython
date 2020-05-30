from pathlib import Path
import json
from scripts.Student import Student

path = str(Path.cwd().parent) + "\\files\\students.json"

file = open(path, 'r')
students = json.load(file)
list = []
for s in students['students']:
    student = Student()
    student.from_json(s)
    list.append(student)

for s in list:
    print(s.toString())

file.close()

