import json
import xml.etree.ElementTree as ET
from scripts.solution_2.Employee import Employee


def read_file(path_xml):
    tree = ET.parse(path_xml)
    root = tree.getroot()
    employees = []
    for e in root.findall('Employee'):
        employee = Employee(e.get('Id'), e.get('Name'), e.get('BasicSalary'), e.get('BonusEachMonth'))
        employees.append(employee)
    return employees


def write_file(path_json, employeeList):
    file = open(path_json, "w")
    employees = {"employees": []}

    for e in employeeList:
        employeeId = getattr(e, "employeeId")
        name = getattr(e, "name")
        salary = e.calculate_total_salary(getattr(e, "basicSalary"), getattr(e, "bonus"))
        employee = Employee(employeeId, name, None, None, salary)
        employees["employees"].append(employee.to_json())

    json.dump(employees, file, indent=4)
