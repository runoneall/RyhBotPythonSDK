import collections
import hashlib
import requests

def Upload(User: str, AvatarPath: str) -> str:

    # Get Avatar Name and Type
    AvatarName = AvatarPath.split("/")[-1]
    AvatarType = AvatarName.split(".")[-1]

    # Get Qiniu Token
    qiniu_token: str = requests.get(
        "https://chat-go.jwzhd.com/v1/misc/qiniu-token",
        headers={
            "Token": User
        }
    ).json()["data"]["token"]

    # Avatar Info
    with open(AvatarPath, "rb") as f:
        file_content = f.read()
    file_key = hashlib.md5(file_content).hexdigest()

    # Upload Avatar to Qiniu
    img_key = requests.post(
        "https://upload-z2.qiniup.com/",
        files=collections.OrderedDict({
            "token": (None, qiniu_token),
            "key": (None, file_key+"."+AvatarType),
            "file": (None, file_content),
            "fname": (None, AvatarName)
        })
    ).json()["key"]

    # Get Avatar URL
    AvatarURL = f"https://chat-img.jwznb.com/{img_key}"
    return AvatarURL