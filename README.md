# LLM Prompt Lab

## Goal

Build a Prompt Engineering experimentation tool to compare different prompt variants across multiple LLMs for real business tasks.

The project aims to evaluate:

- Prompt quality
- Model performance
- Cost
- Latency
- Output quality

The project is designed to evolve throughout the internship, with new capabilities added each week.

## Features

### Version 1

- Run a prompt on a single LLM.
- Display the model response.
- Save raw outputs.

#### Week 1
- Support multiple business tasks.
- Support multiple prompt variants (Zero-shot, Few-shot, Role Prompt).
- Compare two different LLMs.
- Measure latency.
- Estimate token usage and cost (when available).
- Generate Markdown reports.
- Export scoring results.

## Folder Structure

```text
prompt_lab/
├── .venv
│
├── outputs/
│   ├── reports/
│   └── raw_outputs/
│
├── .env
├── .gitignore
├── config.py
├── evaluator.py
├── llm_client.py
├── main.py
├── prompts.py
├── README.md
├── report.py
└── requirements.txt
```
## Project Flow

1- User selects a business task.  
2- User selects a prompt variant.  
3- The application loads the corresponding prompt.  
4- The prompt is sent to the selected LLM.  
5- The model returns a response.  
6- The response is displayed.  
7- Raw outputs are saved.  
8- The response is evaluated.  
9- A report is generated.  


## Future Enhancements

1- Add 2 prompts for Customer Support Email Reply  
2- Add 3 prompts for Meeting Notes Summarization  
3- Add 3 prompts for Ticket Routing  
then  
system prompt  
Interactive Mode: Allow users to provide custom inputs and test prompts manually in addition to predefined evaluation experiments.  
Empower Ticket Routing: If the response can be sent via LLM, it should go to Customer Support Email Reply. If an employee needs to intervene, it should display the ticket details: "Category: , Priority: , Department: , Summary:" by Ticket Routing.  

| Consideration     | Current Status                 | Future Enhancement                

| Model Routing     | Comparing models for each task | Automatic model selection  
| Prompt Injection  | Risk discussion                | Adding a layer of protection before implementing tools  
| Cost Optimization | Cost comparison                | Selecting the most economical model that achieves the required quality  