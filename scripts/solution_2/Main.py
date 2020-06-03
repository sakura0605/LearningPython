from scripts.solution_2.Action import read_file
from scripts.solution_2.Action import write_file

path_xml = "\\Python\\Inheritance_Emplyee\\files\\employee_to_read.xml"
path_json = "\\Python\\Inheritance_Emplyee\\files\\employee_to_write.json"

# print(path_xml, "\n")
# print(path_json)

employees = read_file(path_xml)
write_file(path_json, employees)
