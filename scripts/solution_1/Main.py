from scripts.solution_1.Action import read_file
from scripts.solution_1.Action import write_file
from pathlib import Path

# path_xml = str(Path.cwd().parent) + "\\files\\employee_to_read.xml"
# path_json = str(Path.cwd().parent) + "\\files\\employee_to_write.json"
path_xml = "\\Python\\Inheritance_Emplyee\\files\\employee_to_read.xml"
path_json = "\\Python\\Inheritance_Emplyee\\files\\employee_to_write.json"

employees = read_file(path_xml)
write_file(path_json, employees)
