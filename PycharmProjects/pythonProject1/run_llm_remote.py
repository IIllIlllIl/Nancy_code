import os
from typing import List, Optional
from openai import OpenAI


class ModelPredictor(object):
    def __init__(self, model: str, api_key: str, base_url: Optional[str] = None) -> None:
        self.model = model
        self.api_key = api_key
        self.base_url = base_url
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    def inference_single(self, prompt: str, max_tokens=512):
        completion = self.client.completions.create(
            prompt=prompt,
            model=self.model,
            max_tokens=max_tokens,
        )

        return completion.choices[0].text

    def chat(self, messages: List):
        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model=self.model,
        )
        return chat_completion


model = ModelPredictor("CodeLlama-13b-Python-hf", "fk721027-LMkJNp2jq5tAEE2wC2Mpc2EwHyNEgraY",
                       "http://chat.iteale.com:19017/v1")
out = model.inference_single(
    "def any_int(x, y, z):\n\n    \n    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):\n        if (x+y==z) or (x+z==y) or (y+z==x):\n")
print(out)
