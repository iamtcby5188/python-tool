# main.py

from SftpPwd import SftpPwd


def fromPassWord_xuniji():
    host = "10.10.107.246"
    port = 222
    username = 'admin'
    password = '111111'

    sftpPwd = SftpPwd(host, port)
    trans, sftp = sftpPwd.connect(username, password)
    sftpPwd.loadFileInfo("/")

    try:
        _list = sftp.listdir_attr('/')


        print(f'=========listAttr: [\r\n {_list}\r\n')
    except Exception as aaa:
        print(f'*****list Attr error: {aaa.__traceback__.tb_frame}')
    try:
        a = 1
    except Exception as bbb:
        print(f'*****list Dir error: {bbb}')

    trans.close()
    sftp.close()


if __name__ == '__main__':
    fromPassWord_xuniji()
