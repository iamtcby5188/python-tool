import json
import sys
import threading
import time

from PyCubeCAN import PyCubeCAN
# from busClientTest.message_info import msg_startQuery, msg_QueryPage, msg_QueryIndex,msg_mallocApp
from pywinutil import PyWinUtil

import psutil

def __onRequest(errorCode: int, header: bytes, payload: bytes):
    print(header)
    print(payload)


def __onResponse(errCode: int, header: bytes, payload: bytes):
    # print(header)
    resp = json.loads(payload)
    print(resp)
    # print(resp['params']['page'])
    # print(resp['params']['size'])
    # print(resp['params']['total'])
    # print(resp['params']['totalPage'])
    # print(resp['params']['totalKeyword'])
    # print('--------------------------')
    # print(len(resp['params']['content']))
    # for item in resp['params']['content']:
    #     print(item)


def sendMessage(__can, msg, cmd, toAppType, toAppSession=0):
    try:
        __can.postMessage(cmd, json.dumps(msg).encode(), toAppType, toAppSession)
        time.sleep(1)
    except Exception as e:
        print(e)

def tryEncodeWithANSI(data: str) -> bytes:
    try:
        return data.encode('ansi')
    except Exception as ignore:
        return data.encode()
def busTest():
    __can: PyCubeCAN = None
    __can = PyCubeCAN(b'CubePlatform', 0x0100)
    __can.setAuth(b'admin', b'admin')
    __can.setRequestHandler(__onRequest)
    __can.setResponseHandler(__onResponse)

    pyPath = sys.executable.encode(encoding='utf-8')
    __can.startPrintLog(b'test', pyPath, 0)
    __can.start()
    time.sleep(1)
    # sendMessage(__can, msg_startQuery, 0x07100003, 0x0710)
    while True:
        sendMessage(__can, msg_mallocApp, 0x00010008, 0x0002,0)
    # sendMessage(__can, msg_QueryIndex, 0x07100008, 0x0710)
        time.sleep(10)

def createProcess():
    #cmdLine = tryEncodeWithANSI(r"C:\Program Files\CubeRPA\application\addin_dispatcher\7.8.3\start.cmd")
    cmdLine = tryEncodeWithANSI("C:\\Program Files\\CubeRPA\\application\\cube_agent\\7.9.25\\start.cmd")
    ret, pid, returncode = PyWinUtil.createProcessEx(
        parentPid=0,
        waitExitCode=False,
        lpApplicationName=b'',
        lpCommandLine=cmdLine,
        lpEnvironment=b'',
        lpStartupInfo_dwFlags=b'1',
        lpStartupInfo_wShowWindow=b'0')
    print(f"{ret=},{pid=},{returncode=}")
    try:
        proc = psutil.Process(pid=pid)
        for _subProc in proc.children():
            print(_subProc.pid)
    except Exception as e:
        print(e)

def run_command_in_thread():
    while True:
        createProcess()
        time.sleep(.01)

if __name__ == "__main__":
    thread = threading.Thread(target=run_command_in_thread)
    thread.start()
    thread.join()
