from config import Config
from llm_client import LLMClient
from inputs import INPUTS
from prompt_templates import PROMPT_TEMPLATES
from experiments import EXPERIMENTS, MODELS

client = LLMClient(Config)

results = []

for experiment in EXPERIMENTS:

    task = experiment["task"]
    variant = experiment["variant"]
    input_id = experiment["input_id"]

    prompt = PROMPT_TEMPLATES[task][variant]

    test_case = next(
        item for item in INPUTS[task]
        if item["id"] == input_id
    )

    user_prompt = prompt["user"].format(
        input=test_case["input"]
    )
    for model in MODELS:

        result = client.generate(
            model=model,
            system_prompt=prompt["system"],
            examples=prompt["examples"],
            user_prompt=user_prompt,
            max_tokens=500
        )

        results.append({
            "experiment_id": experiment["id"],
            "task": task,
            "variant": variant,
            "input_id": input_id,
            "model": model,
            "result": result
        })


for result in results:

    print("=" * 70)

    print(
        f"Experiment ID: {result['experiment_id']}\n"
        f"Task: {result['task']}\n"
        f"Variant: {result['variant']}\n"
        f"Input ID: {result['input_id']}\n"
        f"Model: {result['model']}\n"
    )

    print("\nOutput:")
    print(result["result"]["content"])

    print("\nMetrics:")
    print(f"Input tokens: {result['result']['input_tokens']}")
    print(f"Output tokens: {result['result']['output_tokens']}")
    print(f"Total tokens: {result['result']['total_tokens']}")
    print(f"Latency: {result['result']['latency']:.2f}s")
