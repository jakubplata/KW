# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from ksiega_wieczysta import KsiegaWieczysta


class XmlReader(object):

    parse_dict = {'./D1o/R13/E/P2': 'wojewodztwo', './D1o/R13/E/P3': 'powiat', './D1o/R13/E/P4': 'gmina',
                  './D1o/R13/E/P5': 'miejscowosc', './D1o/R13/E/P6': 'dzielnica'}

    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        numer = []
        num = root.findall("./R01/P1")[0]
        for i in ['Wk', 'Nr', 'Ck']:
            numer.append(num.get(i))
        numer = '/'.join(numer)
        kw = KsiegaWieczysta(numer=numer)

        #aktualnie założenie, że jest tylko jedno położenie, często jest innaczej, trzeba będzie zrobić jakiś słownik
        #który dopasuje położenie do konkretnej działki o ile jest przypisane, jak nie to przypisze pierwsze

        for path, attr in self.parse_dict.items():
            val = getattr(kw, attr)
            setattr(kw, attr, root.find(path).get('Tr'))

        print(kw.numer)
        print(kw.wojewodztwo)
        print(kw.powiat)
        print(kw.dzielnica)

        #polozenie = []
        #for i in ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']:
        #    polozenie.append(root.findall("./D1o/R13/E/{}".format(i))[0].get('Tr'))

        #dzialka = root.findall("./D1o/R14/PR141/E/P2".format(i))[0].get('Tr')

        #print(','.join(polozenie))
        #print(dzialka)
        #for child in root:
        #    print(child.tag, child.text)



if __name__ == "__main__":
    xmlreader = XmlReader('./data/RZ1S-00000003-2.xml')
    xmlreader.get_data()
