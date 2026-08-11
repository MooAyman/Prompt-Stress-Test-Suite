INPUTS = {
    "log_triage_summarizer": [
        {
            "id": 1,
            "input": """2026-07-08 03:12:47 [info] 1823#1823: *4518 client 10.12.4.88 connected, request: "POST /v1/agent/analyze HTTP/1.1", host: "api.aibooster.internal"
2026-07-08 03:14:22 [error] 1823#1823: *4521 upstream timed out (110: Connection timed out) while reading response header from upstream, client: 10.12.4.88, server: api.aibooster.internal, request: "POST /v1/agent/analyze HTTP/1.1", upstream: "http://10.12.4.201:8080/v1/agent/analyze", host: "api.aibooster.internal"
2026-07-08 03:14:23 [warn] 1823#1823: *4521 upstream server temporarily disabled while reading response header from upstream, upstream: "http://10.12.4.201:8080/v1/agent/analyze"
2026-07-08 03:14:25 [error] 1823#1823: *4522 connect() failed (111: Connection refused) while connecting to upstream, client: 10.12.4.90, server: api.aibooster.internal, request: "GET /v1/health HTTP/1.1", upstream: "http://10.12.4.201:8080/v1/health"
2026-07-08 03:15:01 [info] 1823#1823: *4525 upstream server 10.12.4.202:8080 re-enabled after health check passed"""
        },
        {
            "id": 2,
            "input": """2026-07-08 02:38:52 INFO [http-nio-8080-exec-14] com.vodafone.aibooster.pipeline.TranscriptProcessor - Starting batch job batch_id=BATCH-88231, transcript_count=452
2026-07-08 02:40:03 WARN [http-nio-8080-exec-14] com.vodafone.aibooster.pipeline.TranscriptProcessor - Heap usage at 87% (3.4GB / 4GB) during batch_id=BATCH-88231
2026-07-08 02:41:09 ERROR [http-nio-8080-exec-14] com.vodafone.aibooster.pipeline.TranscriptProcessor - java.lang.OutOfMemoryError: Java heap space
at com.vodafone.aibooster.pipeline.TranscriptProcessor.processBatch(TranscriptProcessor.java:142)
at com.vodafone.aibooster.pipeline.TranscriptProcessor.run(TranscriptProcessor.java:88)
2026-07-08 02:41:10 INFO [Catalina-utility-1] org.apache.catalina.core.StandardContext - Container restarted automatically, batch_id=BATCH-88231 marked as FAILED, 452 transcripts unprocessed"""
        },
        {
            "id": 3,
            "input": """2026-07-08 08:59:40 INFO WSO2AM - API 'LogAnalysisAgent:v1' invoked by consumer key ending '...93ab', tier 'Gold', client 10.12.7.14, request_id=req-771234
2026-07-08 09:01:12 INFO WSO2AM - Request count for consumer key '...93ab' at 1180/1200 for current 60s window
2026-07-08 09:02:55 WARN WSO2AM - Throttling limit exceeded for API 'LogAnalysisAgent:v1', tier 'Gold', consumer key ending '...93ab'. Request count 1201/1200 for current window.
2026-07-08 09:02:55 ERROR WSO2AM - 429 Too Many Requests returned to client 10.12.7.14, request_id=req-771290
2026-07-08 09:03:00 INFO WSO2AM - Consumer key '...93ab' throttle window reset, requests resuming normally"""
        }
    ],

    "arabic_pii_redaction_checker": [
        {
            "id": 4,
            "input": """الموظف: مساء الخير، مركز خدمة عملاء فودافون، اتفضل.
العميل: مساء النور، أنا أحمد محمود، عايز أستفسر عن فاتورة الشهر ده لأنها زادت عن المعتاد.
الموظف: تمام يا فندم، ممكن أتأكد من رقم الهاتف المسجل على الحساب؟
العميل: أيوه، رقم هاتفي 01012345678، ورقم البطاقة الشخصية بتاعي 29501011234567 لو محتاجاه للتأكيد.
الموظف: تمام يا أستاذ أحمد، وأنا متوفر على نفس الرقم من الساعة 9 صباحًا لحد 5 مساءً لو حصل أي تأخير في الرد."""
        },
        {
            "id": 5,
            "input": """الموظف: أهلًا بيكي، إزاي أقدر أساعدك؟
العميلة: أنا سارة عبد الرحمن، عايزة أغيّر رقم الموبايل المسجل عندكم على حسابي.
الموظف: تمام، ممكن تأكيدي عنوانك الحالي عشان تحديث البيانات؟
العميلة: عنواني هو 12 شارع الجمهورية، الإسكندرية. والرقم القديم المسجل عندكم هو 01123456789، وعايزة أسجل رقم جديد بدل منه.
الموظف: تمام يا فندم، هغيّر الرقم دلوقتي وهبعتلك رسالة تأكيد."""
        },
        {
            "id": 6,
            "input": """الموظف: صباح الخير، حضرتك بتتكلم بالنيابة عن مين؟
المتصل: صباح النور، معايا العميل محمد السيد، رقم الحساب بتاعه 884321، ورقم قوميته 27803152201456.
الموظف: تمام، وحضرتك صلة القرابة إيه بالعميل؟
المتصل: أنا ابنه، وهو عايز يتأكد إن بياناته اتحدّثت صح بعد آخر مكالمة كانت الأسبوع اللي فات.
الموظف: تمام، هراجع الحساب دلوقتي وأأكدلك."""
        }
    ],

    "customer_complaint_reply_drafter": [
        {
            "id": 7,
            "input": """Subject: Overcharged on my last bill — third time reaching out

Hi, I've been a Vodafone customer for over 4 years and this is the first time I've had a real billing problem. I was charged 450 EGP this month instead of my usual 250 EGP plan, with no explanation on the invoice breakdown. I emailed support twice last week (ticket #VF-88213 and a follow-up two days later) and got no reply either time. This is the second time in three months this has happened — last time it took almost three weeks to get a refund. I'm honestly considering switching providers if this isn't resolved quickly. Please explain the charge and refund the difference, and let me know if there's a way to actually get a timely response next time this happens."""
        },
        {
            "id": 8,
            "input": """Subject: No internet for 3 days — two missed technician visits

I work from home and my fiber connection has been completely down since Sunday evening. I scheduled a technician visit for Monday between 2–5pm and nobody showed up or called. I rescheduled for Tuesday morning and the same thing happened again. I've lost three full days of billable work because of this, and every time I call the hotline I'm told 'it's been escalated' but nothing changes. I need someone to actually come out and fix this today, not another promise. Can you confirm a specific time window and give me a direct contact in case it falls through again?"""
        },
        {
            "id": 9,
            "input": """Subject: Replacement SIM never arrived — no tracking info

My SIM card stopped working two weeks ago after I reported it as damaged, and I was told a replacement would be shipped within 3–5 business days. It's now been 14 days with nothing. I've called customer service three times (most recently yesterday) and each time I'm told 'it's on the way' but no one can give me a tracking number, a courier name, or even confirm the shipping address on file is correct. I'm currently without a working number, which is affecting both work and personal contacts trying to reach me. Please either provide real tracking information today or arrange for in-store pickup as an alternative."""
        }
    ]
}