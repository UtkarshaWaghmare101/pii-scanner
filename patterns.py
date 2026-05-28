import re

# Dictionary of PII pattern names and their regex rules
PII_PATTERNS = {
    "Email Address": re.compile(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    ),
    "Phone Number": re.compile(
        r'\b(\+?\d{1,3}[\s\-]?)?(\(?\d{3}\)?[\s\-]?)(\d{3}[\s\-]?\d{4})\b'
    ),
    "IP Address": re.compile(
        r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    ),
    "Hardcoded Password": re.compile(
        r'(password|passwd|pwd|secret)\s*=\s*["\'][^"\']{4,}["\']',
        re.IGNORECASE
    ),
    "API Key / Token": re.compile(
        r'(api_key|apikey|access_token|auth_token)\s*=\s*["\'][a-zA-Z0-9_\-]{16,}["\']',
        re.IGNORECASE
    ),
    "Credit Card Number": re.compile(
        r'\b(?:\d{4}[\s\-]?){3}\d{4}\b'
    ),
}