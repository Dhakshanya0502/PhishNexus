import os
import re

# Suspicious keywords indicating urgency or threat
SUSPICIOUS_KEYWORDS = [
    "urgent", "immediately", "verify", "suspend",
    "locked", "password", "reset", "invoice",
    "payment", "click", "expire"
]

# Generic greetings often used in phishing
GENERIC_GREETINGS = [
    "dear customer",
    "dear user",
    "hello",
]

# Suspicious attachment extensions
SUSPICIOUS_ATTACHMENTS = [
    ".zip", ".exe", ".html"
]

def check_indicators(email_text):
    email_text_lower = email_text.lower()

    indicators = {
        "urgent_language": any(word in email_text_lower for word in SUSPICIOUS_KEYWORDS),
        "generic_greeting": any(greet in email_text_lower for greet in GENERIC_GREETINGS),
        "suspicious_link": bool(re.search(r"http[s]?://", email_text_lower)),
        "suspicious_attachment": any(ext in email_text_lower for ext in SUSPICIOUS_ATTACHMENTS)
    }

    return indicators

def calculate_risk_score(indicators):
    score = 0

    if indicators["urgent_language"]:
        score += 2
    if indicators["generic_greeting"]:
        score += 1
    if indicators["suspicious_link"]:
        score += 3
    if indicators["suspicious_attachment"]:
        score += 3

    if score >= 6:
        return score, "HIGH RISK 🔴"
    elif score >= 3:
        return score, "SUSPICIOUS 🟠"
    else:
        return score, "SAFE 🟢"

def analyze_email(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        email_text = file.read()

    indicators = check_indicators(email_text)
    score, risk_level = calculate_risk_score(indicators)

    print(f"\nAnalyzing: {os.path.basename(file_path)}")
    print("Indicators Found:", indicators)
    print("Risk Score:", score)
    print("Risk Level:", risk_level)
    print("-" * 60)

def main():
    email_folder = "../Sample_Emails"

    if not os.path.exists(email_folder):
        print("Sample_Emails folder not found!")
        return

    for file_name in os.listdir(email_folder):
        if file_name.endswith(".txt"):
            file_path = os.path.join(email_folder, file_name)
            analyze_email(file_path)

if __name__ == "__main__":
    main()