import time
from groq import Groq


class LLMClient:
    def __init__(self,api_key, provider):
        self.api_key = api_key
        self.provider = provider

        if provider == "groq":
            self.client = Groq(api_key=api_key)


    def _build_messages(self, system_prompt, examples, user_prompt):
        messages=[]
        
        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt
                }

            )

        for example in examples:
            messages.append({
                    "role": "user",
                    "content": example["user"]

                })

            messages.append({
                "role": "assistant",
                "content": example["assistant"]
            })

        messages.append({
            "role": "user",
            "content": user_prompt
        })
        return messages


    def generate(self, system_prompt, examples, user_prompt, model, temperature, max_tokens):
        start_time = time.time()
        messages = self._build_messages(
           system_prompt,
            examples,
            user_prompt
            )
        
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )


        end_time = time.time()

        result = {
            "content": response.choices[0].message.content,
            "model": model,
            "tokens": response.usage.total_tokens,
            "latency": end_time - start_time
        }

        return result