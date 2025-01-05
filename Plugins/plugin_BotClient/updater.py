import requests

def update(User:str, Avatar:str, BotId:str, BotName:str, BotDescription:str, SetPrivate:bool=False) -> str:
    response = requests.post(
        "https://chat-go.jwzhd.com/v1/bot/web-edit-bot",
        headers={
            "Token": User
        },
        json={
            "nickname": BotName,
            "introduction": BotDescription,
            "avatarUrl": Avatar,
            "botId": BotId,
            "private": 1 if SetPrivate else 0,
        }
    ).json()["msg"]
    return response