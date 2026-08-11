# Prompt Stress-Test Suite

## Overview

Prompt Stress-Test Suite is a prompt engineering experimentation tool developed to systematically compare different prompt strategies across multiple Large Language Models (LLMs) using real-world business tasks.

## Goal
The goal of the Prompt Stress-Test Suite is to determine how different prompting strategies and LLMs perform across the same business tasks.

The evaluation focuses on three key dimensions:

- Accuracy — How correctly the model handles the task requirements.
- Cost — Estimated API cost based on input and output token usage.
- Latency — Time required to generate the response.

## Experiment Design

The Week 1 experiment consists of:

- 3 real-world business tasks
- 3 prompt variants per task
- 2 LLMs
- 9 inputs
- 18 total experiments

### Business Tasks
1. Log Triage Summarizer
Identifies the main error, likely root cause, and affected component from service logs.

2. Arabic PII Redaction Checker
Detects personally identifiable information in Arabic customer-service transcripts.

3. Customer Complaint Reply Drafter
Generates professional and empathetic first-pass responses to customer complaints.

### Prompt Variants

Each task is tested using three different prompting strategies:

Zero-shot
Few-shot
Role prompting

Each input is paired with one prompt variant, resulting in:

3 Tasks × 3 Prompt Variants = 9 Inputs

9 Inputs × 2 Models = 18 Experiments

### Models

The experiments compare:

- GPT-5.5
- Gemini 3.5 Flash

Both models are evaluated using the same inputs and corresponding prompt variants.

## Evaluation Methodology

Each generated output is evaluated against predefined criteria specific to the task.

The evaluation considers:

### Accuracy

Measures whether the output correctly satisfies the task requirements and remains consistent with the provided input.

### Cost

Estimated using the number of input and output tokens and the corresponding model pricing.

### Latency

Measured as the time between sending the request and receiving the model response.

The final results are compared at both the task level and overall model level.

## Results 
- GPT-5.5 achieved a 2.2 percentage-point accuracy advantage, but was approximately 4.47× more expensive and 3.02× slower in this experiment.

- Gemini 3.5 Flash provided the more efficient overall trade-off, achieving nearly the same accuracy while reducing cost by approximately 77.6% and latency by approximately 66.9%.

## Project Flow

Business Tasks  
      ↓  
9 Predefined Inputs  
      ↓  
Prompt Templates  
      ↓  
3 Prompt Variants  
      ↓  
LLM Client  
      ↓  
GPT-5.5 / Gemini 3.5 Flash  
      ↓  
18 Model Outputs  
      ↓  
Accuracy Evaluation  
      ↓  
Cost & Latency Analysis  
      ↓  
Final Comparison Report  

## Key Findings

The experiment showed that model selection should not be based on accuracy alone.

GPT-5.5 achieved the highest accuracy, but the improvement over Gemini 3.5 Flash was relatively small. Gemini achieved substantially lower cost and latency while maintaining a high level of output quality.

This demonstrates the importance of evaluating LLMs across multiple dimensions when selecting a model for a business use case.

## Technologies
- Python
- OpenAI API
- Google GenAI API
- OpenPyXL
- python-dotenv

## Future Enhancements
- Interactive Mode: Allow users to provide custom inputs.
- Use model routing based on task requirements.
- Selecting the most economical model that achieves the required quality
- Add prompt-injection protection before introducing tool-using workflows.