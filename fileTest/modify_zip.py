import os
import zipfile
import io

sr_path = r"D:\Data\QiyeWei\WXWork\1688851290782214\Cache\File\2024-04\新零售"

modify_file = r"requirements.in"
substring_to_remove = r'sqlalchemy'
import zipfile
import io


def modify_zip_file(file_path, modify_file, substring_to_remove):
    pass
    # 读取压缩文件
    # with zipfile.ZipFile(file_path, 'r') as zip_ref:
    #     for f in zip_ref.infolist():
    #         print(f.filename)
    #     # 读取要修改的文件内容
    #     with zip_ref.open(modify_file) as original_file:
    #         original_content = original_file.read().decode('utf-8')  # 假设文件编码为 utf-8
    #
    #     # 删除包含指定字符串的行
    #     modified_content = ""
    #     for line in original_content.split('\n'):
    #         if substring_to_remove not in line:
    #             modified_content += line + '\n'
    #             print(modified_content)
    #
    #     # 创建一个新的压缩文件
    #     with io.BytesIO() as new_zip_buffer:
    #         with zipfile.ZipFile(new_zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as new_zip:
    #             # 将原始文件以外的文件写入新的压缩文件
    #             for item in zip_ref.infolist():
    #                 if item.filename != modify_file:
    #                     new_zip.writestr(item, zip_ref.read(item.filename))
    #
    #             # 将修改后的文件内容写入新的压缩文件
    #             new_zip.writestr(modify_file, modified_content.encode('utf-8'))  # 写入修改后的内容，假设编码为 utf-8
    #
    #         # 将新的压缩文件内容写回原文件
    #         with open(file_path, 'wb') as f:
    #             f.write(new_zip_buffer.getvalue())


if __name__ == "__main__":
    for root, dirs, files in os.walk(sr_path):
        for file in files:
            file_path = os.path.join(root, file)
            if "new" in file_path:
                print('----------------------------1')
                continue
            print(file_path)
            tmp = file_path.replace(".ppkg", "")
            tmp = tmp.replace('新零售\\', '新零售\\new\\')
            tmp = tmp + "\\" + modify_file
            print(tmp)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                if modify_file in zip_ref.namelist():
                    with zip_ref.open(modify_file) as sr_file:
                        with open(tmp, 'wb') as dst_file:
                            dst_file.write(sr_file.read())
            # modify_zip_file(file_path, modify_file, substring_to_remove)
            print(tmp)
