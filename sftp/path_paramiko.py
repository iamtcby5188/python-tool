import sys

import paramiko.py3compat


__all__ = ['path_paramiko']

PY2 = sys.version_info[0] < 3

if PY2:
    pass
else:
    print('--------------------------- +++')
    def new_u(s, encoding="utf-8"):
        print('----------------------------------')
        if isinstance(s, bytes):
            try:
                return s.decode(encoding)
            except UnicodeDecodeError:
                return s.decode("ISO-8859-1")
        elif isinstance(s, str):
            return s
        else:
            raise TypeError("Expected unicode or bytes, got {!r}".format(s))


    paramiko.py3compat.u = new_u
    import importlib
    import paramiko.message
    importlib.reload(paramiko.message)

class path_paramiko:
    pass
