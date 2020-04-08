# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


class XmlReader(object):

    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()


        numer = []
        num = root.findall("./R01/P1")[0]
        for i in ['Wk', 'Nr', 'Ck']:
            numer.append(num.get(i))


        polozenie = []
        for i in ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']:
            polozenie.append(root.findall("./D1o/R13/E/{}".format(i))[0].get('Tr'))

        dzialka = root.findall("./D1o/R14/PR141/E/P2".format(i))[0].get('Tr')

        print('/'.join(numer))
        print(','.join(polozenie))
        print(dzialka)
        for child in root:
            print(child.tag, child.text)



if __name__ == "__main__":
    xmlreader = XmlReader('./data/RZ1S-00000003-2.xml')
    xmlreader.get_data()
