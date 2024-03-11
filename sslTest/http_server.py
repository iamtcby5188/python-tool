from fastapi import FastAPI
from datetime import datetime
import uvicorn

from constant import https_port, host, need_ssl, certfile, keyfile


class HttpServer:
    app = FastAPI()

    @staticmethod
    @app.get("/time/")
    def read_time():
        return {"time": datetime.now()}

    @staticmethod
    def run():
        try:
            if need_ssl:
                print("---------http------------ssl------------begin")
                uvicorn.run(HttpServer.app, host=host, port=https_port, ssl_keyfile=keyfile, ssl_certfile=certfile)
                print("---------http------------ssl------------end")
            else:
                print("---------http------------no ssl------------begin")
                uvicorn.run(HttpServer.app, host=host, port=https_port)
                print("---------http------------no ssl------------end")
        except Exception as e:
            print("---------http------------------------error")
            print(e)
