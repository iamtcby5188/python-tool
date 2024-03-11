from typing import Tuple


class PyWinUtil:

    @staticmethod
    def getCurrentProcessId() -> int:
        ...

    @staticmethod
    def getCurrentSessionId() -> Tuple[bool, int]:
        ...

    @staticmethod
    def getSessionIdFromPid(pid: int) -> Tuple[bool, int]:
        ...

    @staticmethod
    def isProcessRunAsAdmin() -> bool:
        ...

    @staticmethod
    def isProcessRunAsAdminByPid(pid: int) -> bool:
        ...

    @staticmethod
    def runProcessAsUser(appPath: bytes, params: bytes, isShow: bool) -> Tuple[bool, int, int]:
        ...

    @staticmethod
    def getLastError() -> int:
        ...
