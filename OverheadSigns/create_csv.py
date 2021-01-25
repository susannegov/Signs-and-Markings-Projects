# Original: https://github.com/datitran/raccoon_dataset/blob/master/xml_to_csv.py
# Author: datittran
# This script is modified to split google cloud photos into unassigned
# Google Vision AI csv reading.

import os
import glob
import pandas as pd
from pathlib import Path

def png_to_csv(path):
    png_list = []
    folders = [r'/SignPhotos',r'/SignsFY2019ImageryCropped']
    for f in folders:
        google_url = r'gs://overhead-signs' + f + r'/'
        for file in glob.glob(path + f + '/*.png'):
            value = (google_url + os.path.basename(file),
                     '','','','','','','','','')
            png_list.append(value)
    column_name = ['image_path', 'label', 'x1', 'y1','','','x2', 'y2','','']   
    png_df = pd.DataFrame(png_list,columns=column_name)
    png_df['set'] = 'UNASSIGNED'
    final = png_df.set_index('set')
    return final

def main():
        FILE_PATH = str(Path.cwd())
        png_df = png_to_csv(FILE_PATH)
        png_df.to_csv(FILE_PATH + r'/overhead_signs.csv')
        print('Successfully created csv from png.')

main()
