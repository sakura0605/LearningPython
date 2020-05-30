import json
from scripts.Student import Student
from pathlib import Path

path = str(Path.cwd().parent) + "\\files\\students.json"
file = open(path, "w")

students = {}
students["students"] = []
listStudent = [Student("Cao Hong", 20, 9.9), Student("Ngoc Anh", 18, 7.8), Student("Ngoc Lan", 24, 8.8),
               Student("Thu Thuy", 14, 8.8), Student("An Nhien", 22, 9.8)]

for s in listStudent:
    students["students"].append(s.to_json())

json.dump(students, file, indent=4)
