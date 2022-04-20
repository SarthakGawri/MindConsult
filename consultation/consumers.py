import json
from channels.db import database_sync_to_async
from .models import Consultation, Message
from users.models import User
from channels.generic.websocket import AsyncWebsocketConsumer

""" class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print(self.channel_name)
        print(self.room_group_name)
        #print(self.name)

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.user_id = self.scope['user'].id

        try:
            consultant = User.objects.get(username=self.room_name, is_consultant=True)
        except User.DoesNotExist:
            return

        try:
            patient = User.objects.get(pk=self.user_id, is_patient=True)
        except User.DoesNotExist:
            return

        self.other_group_name = f'chat_{patient.username}'
        # Find consultation object
        try:
            consultation = Consultation.objects.get(patient=patient,consultant=consultant)
        except Consultation.DoesNotExist:
            consultation = Consultation.objects.create(consultant=consultant, patient=patient)

        # Create new message object
        msg = Message(
            consultation=consultation,
            user=self.scope['user'],
            content=message
        )

        msg.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': self.user_id
            }
        )
        async_to_sync(self.channel_layer.group_send)(
            self.other_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': self.user_id
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'user_id': user_id
        }))
 """

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add (
            self.room_group_name,
            self.channel_name
        )
        print(self.channel_name)
        print(self.room_group_name)
        print(self.room_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard (
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.user_id = self.scope['user'].id

        print(self.user_id)
        print(self.room_name)

        try:
            consultant = database_sync_to_async(User.objects.get)(username=self.room_name, is_consultant=True)
        except User.DoesNotExist:
            consultant = database_sync_to_async(User.objects.get)(pk=self.user_id, is_consultant=True)

        """ try:
            patient = database_sync_to_async(User.objects.get)(pk=self.user_id, is_patient=True)
        except User.DoesNotExist:
            patient = database_sync_to_async(User.objects.get)(username=self.name, is_patient=True) """

        # Find consultation object
        #consultation = database_sync_to_async(Consultation.objects.get)(name=self.room_name)
        consultation = await self.get_consultation(consultant=consultant)

        # Create new message object
        await self.create_message(consultation, message)

        #database_sync_to_async(msg.save)()

        # Send message to room group
        await self.channel_layer.group_send (
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': self.user_id
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user_id': user_id
        }))

    @database_sync_to_async
    def get_consultation(self, consultant):
        name = self.room_name
        #consultant = User.objects.get(username=self.room_name)
        return Consultation.objects.get(name=name)

    @database_sync_to_async
    def create_message(self, consultation, message):
        return Message.objects.create(consultation=consultation,
                user=self.scope['user'], content=message)
