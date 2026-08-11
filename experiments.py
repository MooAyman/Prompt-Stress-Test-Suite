EXPERIMENTS = [
    {
        "id": 1,
        "task": "log_triage_summarizer",
        "input_id": 1,
        "variant": "zero_shot"
    },
    {
        "id": 2,
        "task": "log_triage_summarizer",
        "input_id": 2,
        "variant": "few_shot"
    },
    {
        "id": 3,
        "task": "log_triage_summarizer",
        "input_id": 3,
        "variant": "role_prompting"
    },

    {
        "id": 4,
        "task": "arabic_pii_redaction_checker",
        "input_id": 4,
        "variant": "zero_shot"
    },
    {
        "id": 5,
        "task": "arabic_pii_redaction_checker",
        "input_id": 5,
        "variant": "few_shot"
    },
    {
        "id": 6,
        "task": "arabic_pii_redaction_checker",
        "input_id": 6,
        "variant": "role_prompting"
    },

    {
        "id": 7,
        "task": "customer_complaint_reply_drafter",
        "input_id": 7,
        "variant": "zero_shot"
    },
    {
        "id": 8,
        "task": "customer_complaint_reply_drafter",
        "input_id": 8,
        "variant": "few_shot"
    },
    {
        "id": 9,
        "task": "customer_complaint_reply_drafter",
        "input_id": 9,
        "variant": "role_prompting"
    }
]


MODELS = [
    "gpt-5.5",
    "gemini-3.5-flash"
]