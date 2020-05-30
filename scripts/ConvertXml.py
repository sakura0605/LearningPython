import xml.etree.ElementTree as ET

from scripts.Components import Constant
from scripts.Components import Instance
from scripts.Components import Component
from scripts.Components import Components

tree = ET.parse('SystemConstants.table.xml')
root = tree.getroot()

file = open("output.txt", "w")

# Convert XML file to Python object
coms = Components()
for component in root.findall('Component'):
    com = Component()
    com.set_name(component.get('Name'))

    if len(component.findall('Instance')) > 0:
        for instance in component.findall('Instance'):
            ins = Instance(instance.get('Name'))
            for constant in instance.findall('Constant'):
                con = Constant()
                con.set_name(constant.get('Name'))
                ins.add_constants(con)
            com.add_instances(ins)

    if len(component.findall('Constant')) > 0:
        for constant in component.findall('Constant'):
            con = Constant()
            con.set_name(constant.get('Name'))
            com.add_constants(con)
    coms.add_component(com)

# Write in txt file
file.write("There are %d Components. \n" % len(coms.get_components()))
for component in coms.get_components():
    file.write("Component: %s\n" % component.get_name())
    if len(component.get_constants()) == 0:
        file.write("* There is no Constant\n")
    else:
        file.write("* There is/are %d Constant(s)\n" % len(component.get_constants()))
        i = 0
        for constant in component.get_constants():
            i += 1
            file.write("\t%d" % i)
            file.write(". %s\n" % constant.get_name())

    if len(component.get_instances()) == 0:
        file.write("* There is no Instance\n")
    else:
        file.write("* There is/are %d Instance(s)\n" % len(component.get_instances()))
        i = 0
        for instance in component.get_instances():
            i += 1
            file.write("\t%d" % i)
            file.write(". %s\n" % instance.get_name())

            if len(instance.get_constants()) == 0:
                file.write("* There is no Constant inside\n")
            else:
                file.write("\t\tIncluding: %d Constant(s) inside\n" % len(instance.get_constants()))
                j = 0
                for constant in instance.get_constants():
                    j += 1
                    file.write("\t\t%d" % j)
                    file.write(". %s\n" % constant.get_name())

    file.write("---------------------------------------\n")
