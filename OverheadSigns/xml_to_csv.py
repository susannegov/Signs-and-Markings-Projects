# Original: https://github.com/datitran/raccoon_dataset/blob/master/xml_to_csv.py
# Author: datittran
# I imported pathlib and changed path/file names.

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for folder in ['train', 'test']:
        FILE_PATH = str(Path.cwd())
        image_path = FILE_PATH + r'/SignsFY19Labelled'
        #image_path = os.path.join(os.getcwd(), 'SignsFY19Labelled')
        print(image_path)
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(FILE_PATH + "//" + folder + '_overhead_signs.csv', index=None)
        print('Successfully converted xml to csv.')


main()
