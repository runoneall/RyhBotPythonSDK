import requests

def login(email: str, password: str) -> str:
    user_token: str = requests.post(
        "https://chat-go.jwzhd.com/v1/user/email-login",
        json={
            "email": email,
            "password": password,
            "rememberMe": True,
            "platform": "UserBot Client"
        }
    ).json()["data"]["token"]
    return user_token