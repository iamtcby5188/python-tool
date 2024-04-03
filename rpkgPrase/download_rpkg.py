"""
__Type__: script
__Author__: June wang <june.wangj@1data.info>
__CreateDate__: 2022-10-14
__Summary__: 获取oss内指定ppkg文件
__UpdateRecord__:
"""

import oss2
import os
import pandas as pd

# 用户参数
oss_Access_key_id = ''
oss_Access_key_secret = ''

auth = oss2.Auth(oss_Access_key_id, oss_Access_key_secret)
bucket = oss2.Bucket(auth, 'http://oss-cn-shanghai.aliyuncs.com', '1data-prod')

download_src = r'E:\package\testresult\noexist.txt'
result_file_path = r'E:\result'
if os.path.exists(result_file_path):
    pass
else:
    os.makedirs(result_file_path)

with open(download_src, 'r') as f:
    for line in f:

        if ".rpkg" in line:
            line = line.replace('\r','')
            line = line.replace('\n', '')
            strName = line.replace('file/cube_center/', '')
            strName = strName.replace('/', '_')
            ppkg_file_path = os.path.join(result_file_path, strName)

            if os.path.exists(ppkg_file_path):
                pass
            else:
                try:
                    bucket.get_object_to_file(line,ppkg_file_path)
                except oss2.exceptions.NoSuchKey as e:
                    pass
        else:
            pass
print("运行完成")
