import os
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
from xml.dom import minidom


# Read XML
# Open File using filename and absolute path
file_name = 'reed.xml'
full_file = os.path.abspath(os.path.join ('data', file_name))

print(full_file)

# Read File as a doc object model (DOM) for xml parsing
dom = etree.parse(full_file)

# Parse DOM to find tags
courses = dom.findall('course/reg_num')


for c in courses:
    if c.text == "10577":
        print (c.text)
    elif c.text == "20573":
        print (c.text)




# Write XML
# Define Element Tag
dataD = etree.Element('dataD')

# Define Sub-Element Tags
items = etree.SubElement(dataD, 'items')

# Create Sub-Element Tag entries and set ID of entries
item1 = etree.SubElement(items, 'item')
item2 = etree.SubElement(items, 'item')
item1.set ('name', 'item1')
item2.set ('name', 'item2')

# Set value of entries
item1.text = 'item1abc'
item2.text = 'item2abc'

#Print ElementTree - should be a string but prints as binary for some reason
stringTree = etree.tostring(dataD)
print (stringTree)


#Use minidom library to pretty print from Elementree stringObject
xmlstr = minidom.parseString(stringTree).toprettyxml(indent="    ")
#print(xmlstr)

# Open file and write in binary mode
myfile = open("person.xml", 'w')
myfile.write (xmlstr)



