import pefile
from pathlib import Path
from hashlib import sha256
from os import SEEK_END

# filename = r'E:\Code\6.0\Python\py-ccm\dist\ccm_cubeplatform_beta\ccm.exe'
filename = r'E:\Code\6.0\Python\py-ccm\dist\ccm_cubeplatform_prod\ccm.exe'
signature_size: int = 0


def _checksum(data: bytes):
    """
    校验数据
    """
    h = sha256(b"TailStoreSalt")
    h.update(data)
    return h.digest()


def _read_size():
    """
    读取大小
    """
    try:
        with open(filename, 'rb') as f:
            f.seek(-36 - signature_size, SEEK_END)
            size_checksum_bytes = f.read(32)
            size_bytes = f.read(4)
    except (FileNotFoundError, OSError):
        return -1
    if _checksum(size_bytes) == size_checksum_bytes:
        return int.from_bytes(size_bytes, 'little')
    else:
        return -1


def read():
    """
    读取文件尾部
    """
    size = _read_size()
    if size < 0:
        return None
    return _read_data(size)


def find_end():
    """
    找到文件的end位置
    """
    fix_size = len("www.1data.info")
    ret_size = fix_size
    is_finish = False

    while not is_finish:
        try:
            with open(filename, 'rb') as f:
                f.seek(-signature_size - ret_size, SEEK_END)
                data = f.read(fix_size)
                if data == b"www.1data.info":
                    return ret_size
                elif ret_size - fix_size > 200:
                    is_finish = True
                else:
                    ret_size = ret_size + 1
        except:
            pass
    return 0


def _read_data(size: int):
    """
    读取数据
    """
    with open(filename, 'rb') as f:
        f.seek(-68 - size - signature_size, SEEK_END)
        data_checksum_bytes = f.read(32)
        data_bytes = f.read(size)
    if _checksum(data_bytes) == data_checksum_bytes:
        return data_bytes.decode("utf-8")
    else:
        return None


def __get_signature_size(filename):
    try:
        print("----------------------------1")
        pe = pefile.PE(filename, fast_load=True)
        if hasattr(pe, "OPTIONAL_HEADER"):
            optional_header = pe.OPTIONAL_HEADER
            if hasattr(optional_header, "DATA_DIRECTORY"):
                for directory in optional_header.DATA_DIRECTORY:
                    if directory.name == 'IMAGE_DIRECTORY_ENTRY_SECURITY':
                        # 假设directory.Size是签名数据的大小（不包括任何额外的头或尾）
                        if directory.Size > 0:
                            print(f"----------------------------{directory.Size}")
                            return directory.Size

                        # 如果没有找到签名或发生其他情况，返回0
        return 0
    except Exception as e:
        # 打印异常信息以便调试（可选）
        print(f"An error occurred while processing file {filename}: {e}")
        return 0


if __name__ == "__main__":

    pe = pefile.PE(filename, fast_load=True)
    print(pe)
    signature_size = __get_signature_size(filename)

    end_time = find_end()
    signature_size = signature_size + end_time
    print(signature_size)
    data = read()
    print(data)
