def analyze(image_bytes, text, findings, language):
    return {
        "verdict": "Scam",
        "reasons": ["Asks for money", "Creates urgency"],
        "next_steps": ["Do not click links", "Block the sender", "Report it"],
    }