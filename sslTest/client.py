import time

from websocket import WebSocketApp, WebSocket


def __onOpen(ws: WebSocket):
    print(f'open -------------------------------- \r\n')


def __onMessage(ws: WebSocket, data):
    print(f'message -------------------------------- {data = }\r\n')


def __onError(ws: WebSocket, error):
    print(f'__onError -------------------------------- {error = }\r\n')


def __onClose(ws: WebSocket, closeStatusCode: int, closeMsg: str):
    print(f'__onClose -------------------------------- {closeStatusCode=}, { closeMsg= }\r\n')


if __name__ == "__main__":
    # WSS connection
    while True:
        try:
            _wsApp = WebSocketApp(
                url='wss://127.0.0.1:8000',
                on_open=__onOpen,
                on_message=__onMessage,
                on_close=__onClose,
                on_error=__onError
            )

            print('ws new success: ', _wsApp)

            # _wsApp.run_forever()
            _wsApp.run_forever()
            print('ws ------- disconnect --- ')
            time.sleep(2)
        except Exception as e:
            print('exception: ', e)
