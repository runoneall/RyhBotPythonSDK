import requests
import json

Token = ""


def WebSend(api_url, headers, data) -> dict:
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    return json.loads(response.text)


def WebSendFile(api_url, files) -> dict:
    response = requests.request("POST", api_url, files=files)
    return response.json()


def ImageAPI(path: str) -> dict:
    Webhook = "https://chat-go.jwzhd.com/open-apis/v1/image/upload?token="
    api_url = Webhook + Token
    files = [("image", open(path, "rb"))]
    return WebSendFile(api_url, files=files)


def VideoAPI(path: str) -> dict:
    Webhook = "https://chat-go.jwzhd.com/open-apis/v1/video/upload?token="
    api_url = Webhook + Token
    files = [("video", open(path, "rb"))]
    return WebSendFile(api_url, files=files)


def FileAPI(path: str) -> dict:
    Webhook = "https://chat-go.jwzhd.com/open-apis/v1/file/upload?token="
    api_url = Webhook + Token
    files = [("file", open(path, "rb"))]
    return WebSendFile(api_url, files=files)


class Send:
    def __init__(self):
        Webhook = "https://chat-go.jwzhd.com/open-apis/v1/bot/send?token="
        self.api_url = Webhook + Token
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
        }

    def Text(
        self,
        recvId: str,
        recvType: str,
        text: str,
        buttons: list = [],
        parentId: str = None,
    ):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "text",
            "content": {"text": text, "buttons": [buttons]},
        }
        if parentId != None:
            data["parentId"] = parentId
        return WebSend(self.api_url, self.headers, data)

    def Markdown(
        self,
        recvId: str,
        recvType: str,
        markdown: str,
        buttons: list = [],
        parentId: str = None,
    ):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "markdown",
            "content": {"text": markdown, "buttons": [buttons]},
        }
        if parentId != None:
            data["parentId"] = parentId
        return WebSend(self.api_url, self.headers, data)

    def Html(
        self,
        recvId: str,
        recvType: str,
        html: str,
        buttons: list = [],
        parentId: str = None,
    ):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "html",
            "content": {"text": html, "buttons": [buttons]},
        }
        if parentId != None:
            data["parentId"] = parentId
        return WebSend(self.api_url, self.headers, data)

    def Image(
        self,
        recvId: str,
        recvType: str,
        imagePath: str,
        buttons: list = [],
        parentId: str = None,
    ):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "image",
            "content": {
                "imageKey": ImageAPI(imagePath)["data"]["imageKey"],
                "buttons": [buttons],
            },
        }
        if parentId != None:
            data["parentId"] = parentId
        return WebSend(self.api_url, self.headers, data)

    def Video(
        self,
        recvId: str,
        recvType: str,
        videoPath: str,
        buttons: list = [],
        parentId: str = None,
    ):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "video",
            "content": {
                "videoKey": VideoAPI(videoPath)["data"]["videoKey"],
                "buttons": [buttons],
            },
        }
        if parentId != None:
            data["parentId"] = parentId
        return WebSend(self.api_url, self.headers, data)

    def File(
        self,
        recvId: str,
        recvType: str,
        filePath: str,
        buttons: list = [],
        parentId: str = None,
    ):
        data = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "file",
            "content": {
                "fileKey": FileAPI(filePath)["data"]["fileKey"],
                "buttons": [buttons],
            },
        }
        if parentId != None:
            data["parentId"] = parentId
        return WebSend(self.api_url, self.headers, data)


class BatchSend:
    def __init__(self):
        Webhook = "https://chat-go.jwzhd.com/open-apis/v1/bot/batch_send?token="
        self.api_url = Webhook + Token
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
        }

    def Text(
        self,
        recvIds: list[str],
        recvType: str,
        text: str,
        buttons: list = [],
    ):
        data = {
            "recvIds": recvIds,
            "recvType": recvType,
            "contentType": "text",
            "content": {
                "text": text,
                "buttons": [buttons],
            },
        }
        return WebSend(self.api_url, self.headers, data)

    def Markdown(
        self,
        recvIds: list[str],
        recvType: str,
        markdown: str,
        buttons: list = [],
    ):
        data = {
            "recvIds": recvIds,
            "recvType": recvType,
            "contentType": "markdown",
            "content": {
                "text": markdown,
                "buttons": [buttons],
            },
        }
        return WebSend(self.api_url, self.headers, data)

    def Html(
        self,
        recvIds: list[str],
        recvType: str,
        html: str,
        buttons: list = [],
    ):
        data = {
            "recvIds": recvIds,
            "recvType": recvType,
            "contentType": "html",
            "content": {
                "text": html,
                "buttons": [buttons],
            },
        }
        return WebSend(self.api_url, self.headers, data)

    def Image(
        self,
        recvIds: list[str],
        recvType: str,
        imagePath: str,
        buttons: list = [],
    ):
        data = {
            "recvIds": recvIds,
            "recvType": recvType,
            "contentType": "image",
            "content": {
                "imageKey": ImageAPI(imagePath)["data"]["imageKey"],
                "buttons": [buttons],
            },
        }
        return WebSend(self.api_url, self.headers, data)

    def Video(
        self,
        recvIds: list[str],
        recvType: str,
        videoPath: str,
        buttons: list = [],
    ):
        data = {
            "recvIds": recvIds,
            "recvType": recvType,
            "contentType": "video",
            "content": {
                "videoKey": VideoAPI(videoPath)["data"]["videoKey"],
                "buttons": [buttons],
            },
        }
        return WebSend(self.api_url, self.headers, data)

    def File(
        self,
        recvIds: list[str],
        recvType: str,
        filePath: str,
        buttons: list = [],
    ):
        data = {
            "recvIds": recvIds,
            "recvType": recvType,
            "contentType": "file",
            "content": {
                "fileKey": FileAPI(filePath)["data"]["fileKey"],
                "buttons": [buttons],
            },
        }
        return WebSend(self.api_url, self.headers, data)


class Edit:
    def __init__(self):
        Webhook = "https://chat-go.jwzhd.com/open-apis/v1/bot/edit?token="
        self.api_url = Webhook + Token
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
        }

    def Text(
        self, msgId: str, recvId: str, recvType: str, new_text: str, buttons: list = []
    ):
        data = {
            "msgId": msgId,
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "text",
            "content": {"text": new_text, "buttons": [buttons]},
        }
        return WebSend(self.api_url, self.headers, data)

    def Markdown(
        self,
        msgId: str,
        recvId: str,
        recvType: str,
        new_markdown: str,
        buttons: list = [],
    ):
        data = {
            "msgId": msgId,
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "markdown",
            "content": {"text": new_markdown, "buttons": [buttons]},
        }
        return WebSend(self.api_url, self.headers, data)

    def Image(
        self,
        msgId: str,
        recvId: str,
        recvType: str,
        new_image_path: str,
        buttons: list = [],
    ):
        data = {
            "msgId": msgId,
            "recvId": recvId,
            "recvType": recvType,
            "contentType": "image",
            "content": {
                "imageKey": ImageAPI(new_image_path)["data"]["imageKey"],
                "buttons": [buttons],
            },
        }
        return WebSend(self.api_url, self.headers, data)


def Delete(msgId: str, chatId: str, chatType: str):
    Webhook = "https://chat-go.jwzhd.com/open-apis/v1/bot/recall?token="
    api_url = Webhook + Token
    headers = {
        "Content-Type": "application/json; charset=utf-8",
    }
    data = {"msgId": msgId, "chatId": chatId, "chatType": chatType}
    return WebSend(api_url, headers, data)


class Messages:
    def __init__(self):
        Webhook = "https://chat-go.jwzhd.com/open-apis/v1/bot/messages?token="
        self.api_url = Webhook + Token
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
        }

    def Before(self, chat_id: str, chat_type: str, before: int):
        target_url = (
            f"{self.api_url}&chat-id={chat_id}&chat-type={chat_type}&before={before}"
        )
        response = requests.get(target_url, headers=self.headers)
        return json.loads(response.text)

    def After(self, chat_id: str, chat_type: str, message_id: str, after: int):
        target_url = f"{self.api_url}&chat-id={chat_id}&chat-type={chat_type}&message-id={message_id}&after={after - 1}"
        response = requests.get(target_url, headers=self.headers)
        return json.loads(response.text)


class Board:
    def __init__(self):
        Webhook = "https://chat-go.jwzhd.com/open-apis/v1/bot/board?token="
        self.api_url = Webhook + Token
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
        }

    def Text(
        self,
        recvId: str,
        recvType: str,
        text: str,
        expireTime: int = 0,
        memberId: str = "",
    ):
        data = {
            "chatId": recvId,
            "chatType": recvType,
            "contentType": "text",
            "content": text,
        }
        if expireTime != 0:
            data["expireTime"] = expireTime
        if recvType == "group" and memberId != "":
            data["memberId"] = memberId
        return WebSend(self.api_url, self.headers, data)

    def Markdown(
        self,
        recvId: str,
        recvType: str,
        markdown: str,
        expireTime: int = 0,
        memberId: str = "",
    ):
        data = {
            "chatId": recvId,
            "chatType": recvType,
            "contentType": "markdown",
            "content": markdown,
        }
        if expireTime != 0:
            data["expireTime"] = expireTime
        if recvType == "group" and memberId != "":
            data["memberId"] = memberId
        return WebSend(self.api_url, self.headers, data)

    def Html(
        self,
        recvId: str,
        recvType: str,
        html: str,
        expireTime: int = 0,
        memberId: str = "",
    ):
        data = {
            "chatId": recvId,
            "chatType": recvType,
            "contentType": "html",
            "content": html,
        }
        if expireTime != 0:
            data["expireTime"] = expireTime
        if recvType == "group" and memberId != "":
            data["memberId"] = memberId
        return WebSend(self.api_url, self.headers, data)

    def Dismiss(self, recvId: str, recvType: str, memberId: str = ""):
        data = {
            "chatId": recvId,
            "chatType": recvType,
        }
        if recvType == "group" and memberId != "":
            data["memberId"] = memberId
        api_url = (
            f"https://chat-go.jwzhd.com/open-apis/v1/bot/board-dismiss?token={Token}"
        )
        return WebSend(api_url, self.headers, data)

    class All:
        def __init__(self):
            Webhook = "https://chat-go.jwzhd.com/open-apis/v1/bot/board-all?token="
            self.api_url = Webhook + Token
            self.headers = {
                "Content-Type": "application/json; charset=utf-8",
            }

        def Text(self, text: str, expireTime: int = 0):
            data = {
                "contentType": "text",
                "content": text,
            }
            if expireTime != 0:
                data["expireTime"] = expireTime
            return WebSend(self.api_url, self.headers, data)

        def Markdown(self, markdown: str, expireTime: int = 0):
            data = {
                "contentType": "markdown",
                "content": markdown,
            }
            if expireTime != 0:
                data["expireTime"] = expireTime
            return WebSend(self.api_url, self.headers, data)

        def Html(self, html: str, expireTime: int = 0):
            data = {
                "contentType": "html",
                "content": html,
            }
            if expireTime != 0:
                data["expireTime"] = expireTime
            return WebSend(self.api_url, self.headers, data)

        def Dismiss(self):
            api_url = f"https://chat-go.jwzhd.com/open-apis/v1/bot/board-all-dismiss?token={Token}"
            response = requests.post(api_url, headers=self.headers)
            return json.loads(response.text)
