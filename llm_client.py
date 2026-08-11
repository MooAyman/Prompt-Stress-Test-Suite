import time

from openai import OpenAI
from google import genai

class LLMClient:
    def __init__(self, config):
        self.config = config

        self.openai_client = OpenAI(
            api_key=config.OPENAI_API_KEY
        )

        self.gemini_client = genai.Client(
            api_key=config.GEMINI_API_KEY
        )


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
                    "content": example["input"]

                })

            messages.append({
                "role": "assistant",
                "content": example["output"]
            })

        messages.append({
            "role": "user",
            "content": user_prompt
        })
        return messages


    def generate(self, model, system_prompt, examples, user_prompt, max_tokens):

        if model == "gpt-5.5":
            return self._generate_openai(
                model=model,
                system_prompt=system_prompt,
                examples=examples,
                user_prompt=user_prompt,
                max_tokens=max_tokens
            )

        elif model == "gemini-3.5-flash":
            return self._generate_gemini(
                model=model,
                system_prompt=system_prompt,
                examples=examples,
                user_prompt=user_prompt,
                max_tokens=max_tokens
            )

        else:
            raise ValueError(f"Unsupported model: {model}")
    def _generate_openai(self, model, system_prompt, examples, user_prompt, max_tokens):

        start_time = time.time()

        messages = self._build_messages(
           system_prompt,
            examples,
            user_prompt
            )

        response = self.openai_client.chat.completions.create(
            model=model,
            messages=messages,
            max_completion_tokens=max_tokens
        )


        end_time = time.time()

        return {
            "content": response.choices[0].message.content,
            "model": model,
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
            "latency": end_time - start_time
        }

    def _generate_gemini( self, model, system_prompt, examples, user_prompt, max_tokens ):
        start_time = time.time()
        contents = []
        for example in examples:
            contents.append({
                "role": "user",
                "parts": [
                    {
                        "text": example["input"]
                    }
                ]
            })

            contents.append({
                "role": "model",
                "parts": [
                    {
                        "text": example["output"]
                    }
                ]
            })
        contents.append({
            "role": "user",
            "parts": [
                {
                    "text": user_prompt
                }
            ]
        })

        response = self.gemini_client.models.generate_content(
            model=model,
            contents=contents,
            config={
                "system_instruction": system_prompt,
                "max_output_tokens": max_tokens,
                "thinking_config": {
                    "thinking_level": "minimal"
                }
            }
        )
        end_time = time.time()
        usage = response.usage_metadata

        return {
            "content": response.text,
            "model": model,
            "input_tokens": usage.prompt_token_count,
            "output_tokens": usage.candidates_token_count,
            "total_tokens": usage.total_token_count,
            "latency": end_time - start_time
        }