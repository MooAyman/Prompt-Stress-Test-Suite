from config import Config
from llm_client import LLMClient
from prompts import PROMPTS
from experiments import EXPERIMENTS


client = LLMClient(
    Config.API_KEY,
    Config.PROVIDER
)

experiment = EXPERIMENTS[0]

prompt = PROMPTS[experiment["task"]][experiment["variant"]]

user_prompt = prompt["user"].format(input=experiment["input"])

result = client.generate(
    system_prompt=prompt["system"],
    examples=prompt["examples"],
    user_prompt = user_prompt,
    model=experiment["model"],
    temperature=experiment["temperature"],
    max_tokens=experiment["max_tokens"]
)


print(result["content"])
print("\n" + "=" * 50)
print(f"Model: {result['model']}")
print(f"Tokens: {result['tokens']}")
print(f"Latency: {result['latency']:.2f} sec")