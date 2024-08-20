# SftpPwd.py

__all__ = ['SftpPwd']

import sftp.path_paramiko
import paramiko


class SftpPwd:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._trans = None
        self._sftp = None
        self.ssh = None

    def connect(self, username, password):
        try:
            # 实例化一个 transport 对象
            trans = paramiko.Transport((self._host, self._port))
            # 建立连接
            trans.connect(username=username, password=password)
            ssh = paramiko.SSHClient()
            sftp = paramiko.SFTPClient.from_transport(trans)

            self._trans = trans
            self._sftp = sftp

            return trans, sftp

        except Exception as a:
            print(a)
            raise a

    def doDownload(self, _sftp, filepath, localpath):
        pass

    def loadFileInfo(self, folder):
        _dictInfo = []
        try:
            lst = self._sftp.listdir_attr(folder.encode('utf-8'))
            for _file in lst:
                _file_name = _file.filename
                _long_name = _file.longname
                _l_size = len(_long_name)
                if _l_size > 0 and _long_name[0] != 'd':
                    _modify_time = _file.st_mtime
                    _file_size = _file.st_size
                    _dictInfo.append({'fileName': _file_name, 'modify_time': _modify_time, 'file_size': _file_size})
        except Exception as err:
            print(f'load file error: {err}')
        print(str(_dictInfo))

    def getCurrentFileList(self):
        _list = self._sftp.listdir_attr('/')
        return _list

    def download(self, filepath, localpath):
        try:
            lst = self._sftp.listdir_attr('')
            print(f'begin get file...: [{localpath}]')
            self._sftp.get(filepath, localpath)
            print(f'end get file...: [{localpath}]')
        except Exception as a:
            print(a)
            raise a

        return True
