import xml.etree.ElementTree as ET

def read_archive_xspf(path_archive):
    tree = ET.parse(path_archive)
    root = tree.getroot()
    return root
