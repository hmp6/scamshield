import re

def run_rules(text):
    t = text.lower()
    findings = []

    if re.search(r"(pay|fee|deposit|registration|processing charge|send money|transfer|refund|₹\s?\d|rs\.?\s?\d)", t):
        findings.append("Asks for payment or mentions money")

    if re.search(r"[\w.]+@(gmail|yahoo|outlook|hotmail)\.com", t):
        findings.append("Uses a free email (Gmail/Yahoo) instead of a company email")

    if re.search(r"(bit\.ly|tinyurl|t\.co|goo\.gl|cutt\.ly|is\.gd|\.xyz|\.top|\.click)", t):
        findings.append("Contains a shortened or suspicious link")

    if re.search(r"(urgent|immediately|within 24 hours|last chance|blocked|suspended|expire|act now|today only)", t):
        findings.append("Uses urgency or threats")

    if re.search(r"(kyc|otp|pin|cvv|password|aadhaar|pan card|verify your account)", t):
        findings.append("Asks for sensitive details (KYC/OTP/PIN/ID)")

    if re.search(r"(earn|salary|stipend|income).{0,30}(\d{2,3},?\d{3}).{0,30}(per day|daily|weekly|work from home)", t) or "no experience" in t:
        findings.append("Unrealistic pay or no-experience job claim")

    if re.search(r"(parcel|courier|customs|package).{0,40}(held|stuck|pending|fee)", t):
        findings.append("Parcel/courier fee claim")

    return findings

if __name__ == "__main__":
    print(run_rules("URGENT: Your KYC is expired. Pay Rs 10 at bit.ly/xyz or account blocked"))