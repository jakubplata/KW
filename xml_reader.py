# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from ksiega_wieczysta import KsiegaWieczysta
from dzialka import Dzialka

class XmlReader(object):

    def __init__(self, filename):
        self.filename = filename
        self.tree = ET.parse(self.filename)
        self.root = self.tree.getroot()

    def data_collector(self, path, childs):
        data = self.root.findall(path)
        obdata = []
        for element in data:
            collector = []
            for child in childs:
                col_val_data = element.findall(child)
                if len(col_val_data) > 0:
                    for col_val in col_val_data:
                        if col_val.find('D') is None:
                            if 'Ck' in col_val.attrib: # jeśli nie ma treści szukam numeru
                                collector.append(self.get_numer(col_val))
                            elif 'Tr' in col_val.attrib:
                                collector.append(col_val.get('Tr'))
                else:
                    collector.append('---')
            if len(collector) > 1:
                obdata.append(collector)
        return obdata

    def get_numer(self, node):
        numer = []
        for i in ['Wk', 'Nr', 'Ck']:
            numer.append(node.get(i))
        numer = '/'.join(numer)
        return numer

    def kw_get_location(self, kw):
        """
        Metoda pozyskujaca polozenie nieruchomosci dla KW
        :param kw:
        :return:
        """
        paths = ['P' + str(i) for i in range(1, 7)]
        polozenie = self.data_collector('./D1o/R13/E', paths)
        for i in polozenie:
            kw.polozenie[i[0]] = '; '.join(i[1:])

    def kw_get_areas(self, kw):
        # POZYSKANIE DZIALEK
        paths = ['P1', 'P2', 'P3/A', 'P3/B', 'P4/E', 'P5', 'P6', 'P7/A', 'P7/B', 'P8/A',
                 'P8/B', 'P9/A/E', 'P9/B/E', 'P9/C/E', 'P9/D/E']
        attrs = ['id', 'numer', 'nr_obreb', 'nazwa_obreb', 'polozenie', 'ulica', 'korzystanie',
                 'odlczenie_kw', 'odlaczenie_obszar', 'przylaczenie_kw', 'przylaczenie_obszar',
                 'inny_numer']
        dzialki = self.data_collector('./D1o/R14/PR141/E', paths)
        for dz in dzialki:
            dzialka = Dzialka()
            for nr, val in enumerate(dz[0:11]):
                dzialka.__setattr__(attrs[nr], val)
            dzialka.inny_numer = dz[11:]
            kw.dzialki.append(dzialka)



    def get_data(self):
        num = self.root.findall("./R01/P1")[0]
        numer = self.get_numer(num)
        kw = KsiegaWieczysta(numer=numer)

        self.kw_get_location(kw)
        self.kw_get_areas(kw)
        # './R03/P2, jeżeli występień więcej niż jedno to KW zamknięta
        zamknieta = self.root.findall('./R03/P2')
        if len(zamknieta) > 1:
            setattr(kw, 'zamknieta', True)
            setattr(kw, 'zamknieta_tresc', zamknieta[-1].get('Tr'))


        print(kw.numer)
        kw.clear_dzialki()
        for dz in kw.dzialki:
            print(dz.numer, kw.polozenie.get(dz.polozenie, 'BRAK'))




        # NUMERY KW
        # Pole 7 i 9 dzialki


        #paths = ['P1', 'P2/E', 'P3/E', 'P4/A', 'P4/B', 'P5', 'P6', 'P7', 'P8', 'P9',
        #         'P10', 'P11', 'P12', 'P13', 'P14/E/A', 'P14/E/B', 'P15']
        #budynki = self.data_collector('./D1o/R14/PR142/E', paths)
        #if len(budynki) != 0:
        #    print(kw.numer)




        # jeżeli jest więcej niż jedno położenie wówczas jest więce tagów E, P1 to jest numer położenia później powiązany z działką
        """
        for path, attr in self.parse_dict.items():
            val = getattr(kw, attr)
            if len(root.findall(path)) > 1:
                counter = 0
                for elem in root.findall(path):
                    if elem.find('I') is not None:
                        counter += 1
                if counter > 1:
                    print(numer)
        """



            #setattr(kw, attr, root.find(path).get('Tr'))

        #print(kw.numer)
        #print(kw.wojewodztwo)
        #print(kw.powiat)
        #print(kw.dzielnica)

        #polozenie = []
        #for i in ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']:
        #    polozenie.append(root.findall("./D1o/R13/E/{}".format(i))[0].get('Tr'))

        #dzialka = root.findall("./D1o/R14/PR141/E/P2".format(i))[0].get('Tr')

        #print(','.join(polozenie))
        #print(dzialka)
        #for child in root:
        #    print(child.tag, child.text)



if __name__ == "__main__":
    import os
    PATH = 'd:/!!!Roboty/STRZYZOW/01.KW/xml'
    for file in os.listdir(PATH):
        if file.endswith('.xml'):
            fname = os.path.join(PATH, file)
            xmlreader = XmlReader(fname)
            xmlreader.get_data()
