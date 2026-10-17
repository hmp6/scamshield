import json
import ollama

MODEL = "gemma4:e2b"   # must match the name shown by `ollama list`

def analyze(image_bytes, text, findings, language):
    findings_text = "\n".join("- " + f for f in findings) if findings else "- none detected by automatic checks"

    prompt = f"""You are ScamShield, a scam-detection assistant for people in India.
Look at the message (image and/or text below) and decide if it is a scam.

Message text (may be empty if only an image was given):
\"\"\"{text}\"\"\"

Automatic checks found:
{findings_text}

Rules:
- Base your answer ONLY on what is actually in the message and the checks above. Never invent facts.
- verdict must be exactly one of: "Scam", "Suspicious", "Looks safe".
- Use "Scam" only when the message clearly matches a known scam pattern (fake KYC, advance fee, fake job, parcel fee, prize). If it could plausibly be from a real person the user knows, use "Suspicious" and tell them to verify by calling that person.
- Give 2-4 short, simple reasons.
- Give 3-4 practical next steps (e.g. don't click, don't pay, block, report to cybercrime.gov.in or 1930, verify on the official website).

Reply ONLY with JSON in this exact shape:
{{"verdict": "...", "reasons": ["..."], "next_steps": ["..."]}}"""

    message = {"role": "user", "content": prompt}
    if image_bytes:
        message["images"] = [image_bytes]

    try:
        response = ollama.chat(model=MODEL, messages=[message], format="json")
        data = json.loads(response["message"]["content"])
        if data.get("verdict") not in ("Scam", "Suspicious", "Looks safe"):
            data["verdict"] = "Suspicious"
        data.setdefault("reasons", [])
        data.setdefault("next_steps", [])
        return data
    except Exception as e:
        return {
            "verdict": "Suspicious",
            "reasons": [f"Could not fully analyze the message ({e})"],
            "next_steps": ["Do not click links or pay anything", "Verify with the official source"],
        }

if __name__ == "__main__":
    out = analyze(None, "URGENT: Your KYC expired. Pay Rs 10 at bit.ly/xyz or account blocked",
                  ["Uses urgency or threats", "Contains a shortened link"], "English")
    print(json.dumps(out, indent=2, ensure_ascii=False))