import xml.etree.ElementTree as ET

try:
    stream = open("C:/Users/dzygm/OneDrive/Desktop/Schule/Python/Einstieg/Texte/vokabel.txt",mode="rt")
    root = ET.Element('vokabelliste')
    zeile = stream.readline()
    while zeile != '':
        z = zeile.split(';')
        #s = open("C:/Users/dzygm/OneDrive/Desktop/Schule/Python/Einstieg/Texte/vokabel.xml", mode="wt")
        print(z)
        vokabel = ET.SubElement(root, 'vokabel')
        deutsch = ET.SubElement(vokabel, z[0])
        englisch = ET.SubElement(vokabel, z[1])
        tree = ET.ElementTree(root)
        tree.write('vokabel.xml')
        zeile = stream.readline()
except Exception as e:
    print(e)