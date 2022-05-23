import asyncio
import json
from channels.consumer import AsyncConsumer
from random import randint
from time import sleep


class PracticeConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Connected", event)

        await self.send({
            "type": "websocket.accept",
        })

        await self.send({
            "type": "websocket.send",
            "text": 0,
        })

    async def websocket_receive(self, event):
        print("Received", event)

        sleep(1)

        await self.send({
            "type": "websocket.send",
            "text": str(randint(0, 100)),
        })

    async def websocket_disconnect(self, event):
        print("Disconnected", event)