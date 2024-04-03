from pathlib import Path

from rpkgPrase.analysis import _Analysis_Switch, AnalisisException

import pandas as pd
import os

# v = _Analysis_Switch(r'E:\各种现场问题\101_2c9084d8831d20190183412112182aa0.rpkg')
# try:
#     v.visitRpkg()
# except Exception as e:
#     print(e)

excel_files: [] = [r'D:\Data\QiyeWei\WXWork\1688851290782214\Cache\File\2024-01\流程信息240118@卞卞.xlsx',
                   r'D:\Data\QiyeWei\WXWork\1688851290782214\Cache\File\2024-01\组件库信息240118@卞卞.xlsx']

searc_path: str = r'E:\package\rpkg_result_2309_2401'
no_exist_path: str = r'E:\package\testresult\noexist.txt'
rpkg_error: str = r'E:\package\testresult\rpkg_error.txt'


def parse_excel():
    for f in excel_files:
        df = pd.read_excel(f)
        for row in df.iterrows():
            try:
                rpkg = f'{searc_path}\\{row[1][5]}_{row[1][11]}'
                if Path(rpkg).suffix == '.projz':
                    continue

                if os.path.exists(rpkg):
                    try:
                        print(f'visit: {rpkg}')
                        v = _Analysis_Switch(rpkg)
                        v.visitRpkg()
                    except AnalisisException as ee:
                        with open(rpkg_error, 'a') as error_rpkg:
                            error_rpkg.write(
                                f'{row[1][0]}_{row[1][1]}_{row[1][2]}_{row[1][6]}_{row[1][8]}_{row[1][5]}_{row[1][11]}_{ee}\r\n')
                else:
                    with open(no_exist_path, 'a') as no_exist_f:
                        no_exist_f.write(f"file/cube_center/{row[1][5]}/{row[1][11]}\r\n")
            except Exception as e:
                print(e, row)


if __name__ == '__main__':
    parse_excel()
