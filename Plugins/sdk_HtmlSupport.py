WebSend = None
Token = ''

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