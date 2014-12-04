import xml.etree.ElementTree as ET

def parse_config():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    for child in root:
        return str(child.attrib['service']) == 'True'
