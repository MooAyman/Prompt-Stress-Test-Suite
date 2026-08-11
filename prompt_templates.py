PROMPT_TEMPLATES = {

    "log_triage_summarizer": {

        "zero_shot": {
            "system": """
You are an AI assistant that analyzes service logs.
Identify the main error, likely root cause, and affected component.
Return valid JSON only.
""",
            "examples": [],
            "user": """
Analyze the following service log excerpt and produce a structured JSON summary.

Requirements:
- Identify the main error type.
- Identify the likely root cause based only on the provided logs.
- Identify the affected component.
- Do not invent information that is not supported by the logs.
- Return valid JSON only.
- Do not wrap the JSON in markdown code fences.

Required JSON format:
{{
  "error_type": "...",
  "likely_root_cause": "...",
  "affected_component": "..."
}}

Log excerpt:
{input}
"""
        },

        "few_shot": {
            "system": """
You are an AI assistant that analyzes service logs.
Identify the main error, likely root cause, and affected component.
Return valid JSON only.
""",
            "examples": [
                {
                    "input": """
2026-07-01 10:00:01 ERROR payment-service - Database connection timeout
2026-07-01 10:00:02 ERROR payment-service - Unable to process payment
""",
                    "output": """
{
  "error_type": "Database connection timeout",
  "likely_root_cause": "The payment service could not establish a connection to the database within the allowed time.",
  "affected_component": "payment-service"
}
"""
                },
                {
                    "input": """
2026-07-01 11:20:00 WARN api-gateway - Request rate 1050/1000
2026-07-01 11:20:02 ERROR api-gateway - 429 Too Many Requests
""",
                    "output": """
{
  "error_type": "API rate limit exceeded",
  "likely_root_cause": "The request rate exceeded the configured API limit.",
  "affected_component": "api-gateway"
}
"""
                }
            ],
            "user": """
Analyze the following service log excerpt.

Identify:
- error_type
- likely_root_cause
- affected_component

Do not wrap the JSON in markdown code fences.
Return valid JSON only using this format:

{{
  "error_type": "...",
  "likely_root_cause": "...",
  "affected_component": "..."
}}

Log excerpt:
{input}
"""
        },

        "role_prompting": {
            "system": """
You are a senior Site Reliability Engineer specializing in production incident triage.

Your task is to analyze service logs and identify the primary failure.

Follow these rules:
1. Base your analysis strictly on the provided logs.
2. Identify the primary error rather than secondary symptoms.
3. Infer the most likely root cause from the available evidence.
4. Identify the affected service or component.
5. Never invent unavailable information.
6. Return valid JSON only.
""",
            "examples": [],
            "user": """
Analyze this production log excerpt.
Do not wrap the JSON in markdown code fences.
Return exactly this JSON structure:

{{
  "error_type": "...",
  "likely_root_cause": "...",
  "affected_component": "..."
}}

Log excerpt:
{input}
"""
        }
    },


    "arabic_pii_redaction_checker": {

        "zero_shot": {
            "system": """
You are an AI assistant that analyzes Arabic customer-service transcripts.

Identify personally identifiable information (PII) that should be anonymized.
Focus on names, phone numbers, national IDs, account numbers, addresses,
and other clearly identifying personal information.

Extract the exact values as they appear in the transcript.
Return valid JSON only.
""",
            "examples": [],
            "user": """
Analyze the following Arabic customer-service transcript and identify all personally identifiable information (PII) that should be anonymized.

Look for:
- Names
- Phone numbers
- National ID numbers
- Account numbers
- Addresses
- Other clearly identifying personal information

For each entity, provide:
- type
- value
- position

For "position", provide the exact sentence or transcript line where the entity appears.
Do not calculate character offsets or character counts.

Return valid JSON only.
Do not wrap the JSON in markdown code fences.

Required format:
{{
  "entities": [
    {{
      "type": "...",
      "value": "...",
      "position": "..."
    }}
  ]
}}

Transcript:
{input}
"""
        },

        "few_shot": {
            "system": """
You are an AI assistant that analyzes Arabic customer-service transcripts.

Identify personally identifiable information (PII) that should be anonymized.
Focus on names, phone numbers, national IDs, account numbers, addresses,
and other clearly identifying personal information.

Extract the exact values as they appear in the transcript.
Return valid JSON only.
""",
            "examples": [
                {
                    "input": """
العميل: أنا محمد علي، ورقم موبايلي 01012345678.
""",
                    "output": """
{{
  "entities": [
    {{
      "type": "NAME",
      "value": "محمد علي",
      "position": "after 'أنا'"
    }},
    {{
      "type": "PHONE_NUMBER",
      "value": "01012345678",
      "position": "after 'رقم موبايلي'"
    }}
  ]
}}
"""
                },
                {
                    "input": """
العميلة: عنواني 15 شارع النيل، ورقم البطاقة 29501011234567.
""",
                    "output": """
{{
  "entities": [
    {{
      "type": "ADDRESS",
      "value": "15 شارع النيل",
      "position": "after 'عنواني'"
    }},
    {{
      "type": "NATIONAL_ID",
      "value": "29501011234567",
      "position": "after 'رقم البطاقة'"
    }}
  ]
}}
"""
                }
            ],
            "user": """
Identify all PII entities in the following Arabic transcript.

For each entity provide:
- type
- value
- position

For "position", provide the exact sentence or transcript line where the entity appears.
Do not calculate character offsets or character counts.

Do not wrap the JSON in markdown code fences.
Return valid JSON only using this format:

{{
  "entities": [
    {{
      "type": "...",
      "value": "...",
      "position": "..."
    }}
  ]
}}

Transcript:
{input}
"""
        },

        "role_prompting": {
            "system": """
You are a privacy and data-protection specialist responsible for detecting personally identifiable information in Arabic customer-service conversations.

Your job is to identify every piece of PII that should be anonymized.

Pay particular attention to:
- Personal names
- Phone numbers
- National ID numbers
- Account numbers
- Physical addresses

Rules:
1. Extract the exact value as it appears in the transcript.
2. Do not modify or mask the extracted value.
3. Do not classify ordinary non-identifying text as PII.
4. Include the location of each entity.
5. Return valid JSON only.
""",
            "examples": [],
            "user": """
Analyze the following Arabic transcript and identify all PII entities.
For "position", provide the exact sentence or transcript line where the entity appears.
Do not calculate character offsets or character counts.

Do not wrap the JSON in markdown code fences.
Return exactly this JSON structure:

{{
  "entities": [
    {{
      "type": "...",
      "value": "...",
      "position": "..."
    }}
  ]
}}

Transcript:
{input}
"""
        }
    },



    "customer_complaint_reply_drafter": {

        "zero_shot": {
            "system": """
You are an AI assistant that drafts customer support replies.

Write a professional, concise, and empathetic first-pass response.
Acknowledge the customer's issue and propose appropriate next steps.
Do not invent information or make unsupported promises.
""",
            "examples": [],
            "user": """
Draft a professional first-pass customer support reply to the following complaint.

Requirements:
- Acknowledge the customer's issue.
- Show appropriate empathy.
- Address the customer's main concern.
- Propose clear next steps.
- Do not promise a refund, compensation, or resolution unless it is explicitly confirmed.
- Keep the reply to exactly 3 sentences.
- Do not invent information.
- Do not include a subject line or signature.
- Do not claim that you have already taken an action, contacted another team, reviewed an account, or escalated the case unless the customer message explicitly confirms it.

Customer complaint:
{input}
"""
        },

        "few_shot": {
            "system": """
You are an AI assistant that drafts customer support replies.

Write a professional, concise, and empathetic first-pass response.
Acknowledge the customer's issue and propose appropriate next steps.
Do not invent information or make unsupported promises.
""",
            "examples": [
                {
                    "input": """
Subject: Incorrect charge

I was charged 500 EGP instead of my usual 300 EGP plan. Please explain why.
""",
                    "output": """
We’re sorry for the unexpected charge and understand your concern. We’ll review the billing details to determine why the additional amount was applied. Please provide your account or transaction details so we can investigate and update you.
"""
                },
                {
                    "input": """
Subject: Internet outage

My internet has been down since yesterday and I need it for work. Please fix this as soon as possible.
""",
                    "output": """
We’re sorry for the disruption and understand how important your internet connection is for your work. We’ll check the status of the service issue and coordinate the appropriate technical support. Please provide your account number so we can locate your service and provide an update.
"""
                }
            ],
            "user": """
Draft a professional first-pass reply to this customer complaint.

The reply must:
- Acknowledge the issue.
- Show empathy.
- Propose next steps.
- Avoid unsupported promises.
- Contain exactly 3 sentences.
- Include no subject line or signature.
- Do not claim that you have already taken an action, contacted another team, reviewed an account, or escalated the case unless the customer message explicitly confirms it.

Customer complaint:
{input}
"""
        },

        "role_prompting": {
            "system": """
You are a senior customer support representative handling customer complaints.

Write concise, professional, and empathetic first-pass responses.

Your response must:
1. Acknowledge the customer's specific complaint.
2. Demonstrate appropriate empathy without sounding overly formal.
3. Propose realistic next steps based only on the information provided.
4. Never promise refunds, compensation, deadlines, or resolutions that are not confirmed.
5. Avoid generic corporate language.
6. Contain exactly 3 sentences.
7. Do not include a subject line or signature.
""",
            "examples": [],
            "user": """
Write a first-pass response to the following customer complaint.
Do not claim that you have already taken an action, contacted another team, reviewed an account, or escalated the case unless the customer message explicitly confirms it.

Customer complaint:
{input}
"""
        }
    }
}