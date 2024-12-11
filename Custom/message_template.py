header = '''
import requests
import json

Token = ''


def WebSend(api_url, headers, data) -> dict:
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    return json.loads(response.text)


def ImageAPI(path: str) -> str:
    Webhook = "https://chat-go.jwzhd.com/open-apis/v1/image/upload?token="
    api_url = Webhook + Token
    files=[
        ('image',open(path,'rb'))
    ]
    response = requests.request("POST", api_url, files=files)
    return response.json()
'''

send_class_header = '''
class Send:
    def __init__(self):
        Webhook = 'https://chat-go.jwzhd.com/open-apis/v1/bot/send?token='
        self.api_url = Webhook + Token
        self.headers = {"Content-Type": "application/json; charset=utf-8", }
'''

send_text = '''
    def Text(self, recvId: str, recvType: str, text: str, buttons: list = [], parentId: str = None):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "text",
            "content": {
                "text": text,
                "buttons": [buttons]
            }
        }
        if parentId != None:
            data["parentId"] = parentId
        return WebSend(self.api_url, self.headers, data)
'''

send_markdown = '''
    def Markdown(self, recvId: str, recvType: str, markdown: str, buttons: list = [], parentId: str = None):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "markdown",
            "content": {
                "text": markdown,
                "buttons": [buttons]
            }
        }
        if parentId != None:
            data["parentId"] = parentId
        return WebSend(self.api_url, self.headers, data)
'''

send_image = '''
    def Image(self, recvId: str, recvType: str, imagePath: str, buttons: list = [], parentId: str = None):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "image",
            "content": {
                "imageKey": ImageAPI(imagePath)["data"]["imageKey"],
                "buttons": [buttons]
            }
        }
        if parentId != None:
            data["parentId"] = parentId
        return WebSend(self.api_url, self.headers, data)
'''

send_file = '''
    def File(self, recvId: str, recvType: str, fileName: str, fileUrl: str, buttons: list = [], parentId: str = None):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "file",
            "content": {
                "fileName": fileName,
                "fileUrl": fileUrl,
                "buttons": [buttons]
            }
        }
        if parentId != None:
            data["parentId"] = parentId
        return WebSend(self.api_url, self.headers, data)
'''

edit_class_header = '''
class Edit:
    def __init__(self):
        Webhook = 'https://chat-go.jwzhd.com/open-apis/v1/bot/edit?token='
        self.api_url = Webhook + Token
        self.headers = {"Content-Type": "application/json; charset=utf-8", }
'''

edit_text = '''
    def Text(self, msgId: str, recvId: str, recvType: str, new_text: str, buttons: list = []):
        data = {
            "msgId": msgId,
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "text",
            "content": {
                "text": new_text,
                "buttons": [buttons]
            }
        }
        return WebSend(self.api_url, self.headers, data)
'''

edit_markdown = '''
    def Markdown(self, msgId: str, recvId: str, recvType: str, new_markdown: str, buttons: list = []):
        data = {
            "msgId": msgId,
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "markdown",
            "content": {
                "text": new_markdown,
                "buttons": [buttons]
            }
        }
        return WebSend(self.api_url, self.headers, data)
'''

edit_image = '''
    def Image(self, msgId: str, recvId: str, recvType: str, new_image_path: str, buttons: list = []):
        data = {
            "msgId": msgId,
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "image",
            "content": {
                "imageKey": ImageAPI(new_image_path)["data"]["imageKey"],
                "buttons": [buttons]
            }
        }
        return WebSend(self.api_url, self.headers, data)
'''

edit_file = '''
    def File(self, msgId: str, recvId: str, recvType: str, new_file_name: str, new_file_url: str, buttons: list = []):
        data = {
            "msgId": msgId,
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "file",
            "content": {
                "fileName": new_file_name,
                "fileUrl": new_file_url,
                "buttons": [buttons]
            }
        }
        return WebSend(self.api_url, self.headers, data)
'''

message_class_header = '''
class Messages:
    def __init__(self):
        Webhook = 'https://chat-go.jwzhd.com/open-apis/v1/bot/messages?token='
        self.api_url = Webhook + Token
        self.headers = {"Content-Type": "application/json; charset=utf-8", }
'''

message_before = '''
    def Before(self, chat_id: str, chat_type: str, before: int):
        target_url = f"{self.api_url}&chat-id={chat_id}&chat-type={chat_type}&before={before}"
        response = requests.get(target_url, headers=self.headers)
        return json.loads(response.text)
'''

message_after = '''
    def After(self, chat_id: str, chat_type: str, message_id: str, after: int):
        target_url = f"{self.api_url}&chat-id={chat_id}&chat-type={chat_type}&message-id={message_id}&after={after - 1}"
        response = requests.get(target_url, headers=self.headers)
        return json.loads(response.text)
'''

board_user_class_header = '''
class Board:
    def __init__(self):
        Webhook = 'https://chat-go.jwzhd.com/open-apis/v1/bot/board?token='
        self.api_url = Webhook + Token
        self.headers = {"Content-Type": "application/json; charset=utf-8", }
'''

board_user_text = '''
    def Text(self, recvId: str, recvType: str, text: str, expireTime: int = 0):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "text",
            "content": text,
        }
        if expireTime != 0:
            data["expireTime"] = expireTime
        return WebSend(self.api_url, self.headers, data)
'''

board_user_markdown = '''
    def Markdown(self, recvId: str, recvType: str, markdown: str, expireTime: int = 0):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "markdown",
            "content": markdown,
        }
        if expireTime != 0:
            data["expireTime"] = expireTime
        return WebSend(self.api_url, self.headers, data)
'''

board_user_html = '''
    def Html(self, recvId: str, recvType: str, html: str, expireTime: int = 0):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "html",
            "content": html,
        }
        if expireTime != 0:
            data["expireTime"] = expireTime
        return WebSend(self.api_url, self.headers, data)
'''

board_user_cancel = '''
    def Dismiss(self, recvId: str, recvType: str):
        data = {
            "recvId": recvId,
            "recvType": recvType,
        }
        api_url = f'https://chat-go.jwzhd.com/open-apis/v1/bot/board-dismiss?token={Token}'
        return WebSend(api_url, self.headers, data)
'''

board_global_class_header = '''
    class All:
        def __init__(self):
            Webhook = 'https://chat-go.jwzhd.com/open-apis/v1/bot/board-all?token='
            self.api_url = Webhook + Token
            self.headers = {"Content-Type": "application/json; charset=utf-8", }
'''

board_global_text = '''
        def Text(self, text: str, expireTime: int = 0):
            data = {
                "contentType": "text",
                "content": text,
            }
            if expireTime != 0:
                data["expireTime"] = expireTime
            return WebSend(self.api_url, self.headers, data)
'''

board_global_markdown = '''
        def Markdown(self, markdown: str, expireTime: int = 0):
            data = {
                "contentType": "markdown",
                "content": markdown,
            }
            if expireTime != 0:
                data["expireTime"] = expireTime
            return WebSend(self.api_url, self.headers, data)
'''

board_global_html = '''
        def Html(self, html: str, expireTime: int = 0):
            data = {
                "contentType": "html",
                "content": html,
            }
            if expireTime != 0:
                data["expireTime"] = expireTime
            return WebSend(self.api_url, self.headers, data)
'''

board_global_cancel = '''
        def Dismiss(self):
            api_url = f'https://chat-go.jwzhd.com/open-apis/v1/bot/board-all-dismiss?token={Token}'
            response = requests.post(api_url, headers=self.headers)
            return json.loads(response.text)
'''

delete = '''
def Delete(msgId: str, chatId: str, chatType: str):
    Webhook = 'https://chat-go.jwzhd.com/open-apis/v1/bot/recall?token='
    api_url = Webhook + Token
    headers = {"Content-Type": "application/json; charset=utf-8", }
    data = {
        "msgId": msgId,
        "chatId": chatId,
        "chatType": chatType
    }
    return WebSend(api_url, headers, data)
'''