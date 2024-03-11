import json
import sys
import time

from PyCubeCAN import PyCubeCAN


def __onRequest(errorCode: int, header: bytes, payload: bytes):
    print(header)
    print(payload)


def __onResponse(errCode: int, header: bytes, payload: bytes):
    print(header)
    print(payload)


__can: PyCubeCAN = None
__can = PyCubeCAN(b'CubePlatform', 0x0222)
__can.setAuth(b'admin', b'admin')
__can.setRequestHandler(__onRequest)
__can.setResponseHandler(__onResponse)

pyPath = sys.executable.encode(encoding='utf-8')
__can.startPrintLog(b'ns', pyPath, 0)
__can.start()

while True:
    try:
        dic = {"cmd_code": 83951681,
               "req_id": 107,
               "options": {
                   "studio_browser_id": "StudioPage_3",
                   "command": "product-show",
                   "fetch": True,
                   "token": "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4MTMiLCJiZWxvbmciOiJjdXN0b21lci1zc28iLCJsb2dpbkFwcCI6MTAwMDAxLCJpc3MiOiJzc28iLCJpc01vYmlsZSI6ZmFsc2UsInNlc3Npb25JZCI6IjdkNTI1ODY0OWM0MzRlNTVhYjA2NmY0YTA0MWJjNTA3IiwidHlwZSI6ImJ1c2luZXNzIiwiZXhwIjoxNzA5NTczMzAxLCJ1c2VySWQiOjgxMywiaWF0IjoxNzA5NTMwMTAxfQ.Xy_fbjH0gccTny0Mm7_Uo1aWOsvVAwoqU4ijpPWxDrgjR_DK5UG6TXzHUlPja3pJ_jsRxpT1N5jp13aFrVuPOJQKgOdarRP7FY8D2weFd8RJu5142LgkxuvHIompHgAs5Lgtf04Jw3W_pSAuGp2oNkLhl7fSs82MUbPlk5oyaow"
               }
               }
        __can.postMessage(0x0001FF00, json.dumps(dic).encode(), 0x0501,0)
        time.sleep(1)
    except Exception as e:
        print(e)
