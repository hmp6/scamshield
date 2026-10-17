import json
from rules import run_rules

samples = json.load(open("tests/samples.json", encoding="utf-8"))
correct = 0
for s in samples:
    findings = run_rules(s["text"])
    predicted = "scam" if len(findings) >= 2 else "genuine"
    ok = predicted == s["label"]
    correct += ok
    print("OK " if ok else "WRONG", s["label"], findings)
print(f"\nCorrect: {correct}/{len(samples)}")