import threading
import time

from websocket import WebSocketApp, WebSocket


stop_flg = False


def sendTest(wsApp):
    while not stop_flg:
        try:
            time.sleep(1)
            print('sendTest---')
            wsApp.send('hi')
        except Exception as e:
            print(e)

    print(stop_flg, '-------------------------------')


def __onOpen(ws: WebSocket):
    print(f'open -------------------------------- \r\n')

    thd = threading.Thread(target=sendTest, args=[ws, ])
    thd.start()


def __onMessage(ws: WebSocket, data):
    print(f'message -------------------------------- {data = }\r\n')


def __onError(ws: WebSocket, error):
    print(f'__onError -------------------------------- {error = }\r\n')
    stop_flg=True


def __onClose(ws: WebSocket, closeStatusCode: int, closeMsg: str):
    print(f'__onClose -------------------------------- {closeStatusCode=}, { closeMsg= }\r\n')
    stop_flg=True


if __name__ == "__main__":
    # WSS connection
    while True:
        try:
            header = {'serverVersion': "1.1.1"}
            stop_flg = False
            _wsApp = WebSocketApp(
                url='wss://www.1datallm.com:443',
                header=header,
                on_open=__onOpen,
                on_message=__onMessage,
                on_close=__onClose,
                on_error=__onError
            )

            print('ws new success: ', _wsApp)

            # _wsApp.run_forever()
            _wsApp.run_forever()
            stop_flg = True

            print('ws ------- disconnect --- ')
            time.sleep(2)
        except Exception as e:
            print('exception: ', e)
