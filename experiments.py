EXPERIMENTS = [
    {
        "input": """
        Customer Name: Ahmed

        Subject: Payment Deducted but Bill Still Unpaid

        Message:
        I paid my electricity bill through the AMAN app, and the payment was deducted from my account, but the bill is still showing as unpaid. Please help.
        """,
        "task": "customer_support_email_reply",
        "variant": "zero_shot",                      # "zero_shot", "few_shot", "role_prompting"
        "model": "llama-3.1-8b-instant",
        "temperature": 0.3,
        "max_tokens": 300
    }
]