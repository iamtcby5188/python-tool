import asyncio
import datetime
import json
import threading
import time
import ssl

import websockets

from constant import certfile, keyfile, host, ws_port, need_ssl


class WSServer:
    clients: list = []

    @staticmethod
    async def s(msg, ws):
        await WSServer.sendMsg(msg, ws)

    @staticmethod
    async def sendMsg(msg, ws):
        if ws:
            await ws.send(msg)

        await asyncio.sleep(.01)

    @staticmethod
    async def broadcastMsg(msg):
        for user in WSServer.clients:
            await user.send(msg)

    @staticmethod
    async def echo(websocket, path):
        print(f'------------echo{path}')
        WSServer.clients.append(websocket)
        await websocket.send(json.dumps({'type': 'hello'}))
        while True:
            try:
                time.sleep(.01)
                recv_text = await websocket.recv()
                print(recv_text)
            except websockets.ConnectionClosed:
                print('connect closed.....', path)
                WSServer.clients.remove(websocket)
                break
            except websockets.InvalidState:
                print('websocket invalid state...')
                WSServer.clients.remove(websocket)
                break
            except Exception as e:
                print(e)
                WSServer.clients.remove(websocket)
                break

    @staticmethod
    async def runServer():
        if need_ssl:
            print("---------runServer------------ssl------------begin")
            print(certfile)
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ssl_context.load_cert_chain(certfile, keyfile)

            async with websockets.serve(WSServer.echo, host, ws_port, ssl=ssl_context):
                await asyncio.Future()

            print("---------runServer------------ssl------------end")
        else:
            print("---------runServer------------no ssl------------begin")
            async with websockets.serve(WSServer.echo, host, ws_port):
                await asyncio.Future()
            print("---------runServer------------no ssl------------end")

    @staticmethod
    def websocketServer():
        asyncio.run(WSServer.runServer())

    @staticmethod
    def run():
        try:
            thread = threading.Thread(target=WSServer.websocketServer)
            thread.start()
            thread.join()

        except Exception as e:
            print("---------ws------------------------error")
            print(e)
