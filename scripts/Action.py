import json
import xml.etree.ElementTree as ET
from scripts.Employee import Employee


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
        employee = Employee()
        setattr(employee, "employeeId", getattr(e, "employeeId"))
        setattr(employee, "name", getattr(e, "name"))
        total = e.calculate_total_salary(getattr(e, "basicSalary"), getattr(e, "bonus"))
        setattr(employee, "totalSalary", total)
        employees["employees"].append(employee.to_json())

    json.dump(employees, file, indent=4)
