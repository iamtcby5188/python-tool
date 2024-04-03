import rarfile
rarfile.UNRAR_TOOL='D:\\unrar.exe'

if __name__ == '__main__':
    file_path = r"D:\Data\QiyeWei\WXWork\1688851290782214\Cache\File\2024-03\222.rar"
    extract_path = r"D:\Data\QiyeWei\WXWork\1688851290782214\Cache\File\2024-03\123"

    with rarfile.RarFile(file_path, 'r') as rar_ref:
        rar_ref.extractall(extract_path)