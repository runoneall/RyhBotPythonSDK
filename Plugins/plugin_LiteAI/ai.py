from openai import OpenAI

zhipu_api_key = ""
xinghuo_api_password = ""


class ChatClient:
    def __init__(self):
        self.zhipu = OpenAI(
            api_key=zhipu_api_key,
            base_url="https://open.bigmodel.cn/api/paas/v4/",
        )
        self.xinghuo = OpenAI(
            api_key=xinghuo_api_password,
            base_url="https://spark-api-open.xf-yun.com/v1",
        )

    def zhipu_chat(self, query: str, history: list[dict[str, str]] = [], **kwargs):
        history.append({"role": "user", "content": query})
        response = self.zhipu.chat.completions.create(
            model="glm-4-flash", messages=history, stream=True, **kwargs
        )
        for chunk in response:
            yield chunk

    def xinghuo_chat(self, query: str, history: list[dict[str, str]] = [], **kwargs):
        history.append({"role": "user", "content": query})
        response = self.xinghuo.chat.completions.create(
            model="lite", messages=history, stream=True, **kwargs
        )
        for chunk in response:
            yield chunk

    def web_search(self, query: str):
        query = "搜索并总结：" + query
        response = self.xinghuo_chat(query, max_tokens=4096, top_p=1.0, temperature=1.0)
        for chunk in response:
            yield chunk.choices[0].delta.content

    def image_vision(self, query: str, image_url: str):
        response = self.zhipu.chat.completions.create(
            model="glm-4v-flash",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "image_url", "image_url": {"url": image_url}},
                        {"type": "text", "text": query},
                    ],
                }
            ],
            stream=True,
            max_tokens=1024,
            top_p=1.0,
            temperature=1.0,
        )
        for chunk in response:
            yield chunk.choices[0].delta.content
    
    def image_generation(self, query: str, width: int, height: int):
        response = self.zhipu.images.generate(
            model="cogview-3-flash",
            prompt=query,
            size=f"{width}x{height}",
        )
        return response.data[0].url