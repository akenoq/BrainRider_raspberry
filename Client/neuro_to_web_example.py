import asyncio
import random

from autobahn.asyncio.websocket import WebSocketClientProtocol, WebSocketClientFactory


class MyClientProtocol(WebSocketClientProtocol):

    def onConnect(self, response):
        print("Server connected: {0}".format(response.peer))

    async def onOpen(self):
        NEURO_MODE = ["FIRST", "SECOND"]
        print("WebSocket connection open.")
        # start sending messages every 500ms ..
        while True:
            # sending mode
            mode_neuro = random.choice(NEURO_MODE)
            # self.sendMessage(mode_neuro.encode('utf8'))

            # sending data
            number_of_points = random.randint(1, 32)
            arr = []
            for i in range(0, number_of_points):
                arr.append(str(random.randint(-128, 128)))

            # str for sending => 10 20 30 ...
            data = " ".join(arr)
            self.sendMessage(data.encode('utf8'))


    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            print("Text message received: {0}".format(payload.decode('utf8')))

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))


if __name__ == '__main__':

    factory = WebSocketClientFactory(u"ws://node-ws-server-neuro.eu-gb.mybluemix.net:80")
    factory.protocol = MyClientProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_connection(factory, 'node-ws-server-neuro.eu-gb.mybluemix.net', 80)
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()
