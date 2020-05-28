from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

# Chat 모델에 데이터가 추가되면 이 정보를 웹소켓이 연결된 페이지에 보내는 코드 작성
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.group = self.scope['url_route']['kwargs']['room']
        self.groupname = 'chat_%s' % self.group
        print('connect')

        async_to_sync(self.channel_layer.group_add)(
            self.groupname,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        print('disconnect')
        async_to_sync(self.channel_layer.group_discard)(
            self.groupname,
            self.channel_name
        )

    # WebSocket 으로부터 message 수신
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        author = text_data_json['author']
        message = text_data_json['message']
        created_at = text_data_json['created_at']
        print("Consumer receive message: ", author, message, created_at)

        # room 으로 message 전송
        async_to_sync(self.channel_layer.group_send)(
            self.groupname,
            {
                'type': 'chat_message',
                'author': author,
                'message': message,
                'created_at': created_at
            }
        )

    # room 으로부터 message 수신
    def chat_message(self, event):
        author = event['author']
        message = event['message']
        created_at = event['created_at']
        print("Send message: ", author, message, created_at)

        # WebSocket 으로 message 전송
        self.send(text_data=json.dumps({
            'author': author,
            'message': message,
            'created_at': created_at
        }))