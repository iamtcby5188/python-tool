import time
from concurrent.futures import ThreadPoolExecutor

from http_server import HttpServer
from ws_server import WSServer



class SSLServer:
    def __init__(self):
        self.__threadpool = ThreadPoolExecutor(max_workers=6, thread_name_prefix='SSLServer')

    def __startHttp(self):
        print('HttpServer.run --- begin')
        HttpServer.run()
        print('HttpServer.run --- end')

    def __startWss(self):
        print('WSServer.run --- begin')
        WSServer.run()
        print('WSServer.run --- end')

    def run(self):
        self.__threadpool.submit(self.__startHttp)
        self.__threadpool.submit(self.__startWss)

        while True:
            time.sleep(.01)


if __name__ == "__main__":
    SSLServer().run()
