import xmlschema
xml_file = "Web Stack\Assignment 4\employees.xml"
xsd_file = "Web Stack\Assignment 4\employee_schema.xsd"

validator = xmlschema.XMLSchema(xsd_file)
if validator.is_valid(xml_file):
    print("XML file is valid.")
else:
    print("XML file is not valid.")
    print(validator.validate(xml_file))