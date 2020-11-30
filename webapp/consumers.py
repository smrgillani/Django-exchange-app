# """Manage websocket connections."""

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .BL.ConversionsBL import ConversionsBL as cnbl

class ConversionConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        user = self.scope["user"]
        self.group_name = 'exchange-{}'.format(user.id)

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        await self.send_all_conversions()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    @sync_to_async
    def getAllConversions(self):
        user = self.scope["user"]
        return cnbl.allConversions(user.id)

    async def send_all_conversions(self):
        
        for cnvrns in await self.getAllConversions():

            message = {
                'cnvOps': 'add',
                'cnvId': cnvrns.Id,
                'fromShortName': cnvrns.currencyFromShortName,
                'toShortName': cnvrns.currencyToShortName,
                'cnvRate': cnvrns.rate,
            }

            await self.channel_layer.group_send(self.group_name,
                {
                    'type': 'send_message',
                    'text': message}
            )

    async def send_message(self, event):
        message = event['text']

        # Send message to WebSocket
        await self.send(text_data=json.dumps(
            message
        ))