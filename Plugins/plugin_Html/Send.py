import json
import requests
Token = ''

def WebSend(api_url, headers, data) -> dict:
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    return json.loads(response.text)

def SendHtml(recvId:str, recvType:str, html:str):
    BaseUrl = 'https://chat-go.jwzhd.com/open-apis/v1/bot/send?token='
    api_url = BaseUrl+Token
    headers = {"Content-Type": "application/json; charset=utf-8",}
    data = {
        "recvId": recvId,
        "recvType": recvType,
        "contentType": "html",
        "content": {
            "text": html
        }
    }
    return WebSend(api_url,headers,data)