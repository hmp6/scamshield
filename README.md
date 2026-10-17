# ScamShield 🛡️

Checks suspicious WhatsApp/SMS messages and screenshots (UPI, KYC, parcel fees, fake jobs and internships) and explains the risk in English, Hindi or Malayalam.

## How it works
1. Fixed rule checks flag red flags: payment requests, Gmail/Yahoo senders, shortened links, urgency, sensitive-info requests, unrealistic pay.
2. Gemma reads the screenshot or text plus those findings, then returns a verdict (Scam / Suspicious / Looks safe), reasons and next steps.
3. Gemma is told to explain only the evidence it is given, not to invent findings.

## Model
- **Gemma 4 E2B** (open-weight), run locally through Ollama (`gemma4:e2b`)
- Model card: (https://ollama.com/library/gemma4:e2b)
- License/terms: (https://policies.google.com/terms)

## Dependencies
Python 3.10+, Streamlit, Ollama (Python library and app)

## Run it
1. Install Ollama from ollama.com and run `ollama pull gemma4:e2b`
2. `pip install -r requirements.txt`
3. `streamlit run app.py`
4. Open http://localhost:8501

## Results
Rule checks alone got 15 of 15 test messages right (see `tests/samples.json`, run `python test_rules.py`).
Full app (rules + Gemma): 15 of 15.

## Limitations
- Guidance only, not a guarantee. A "Looks safe" verdict does not prove a message is genuine.
- Hindi and Malayalam output may contain errors.
- Runs locally, so speed depends on your laptop.

## Team
Hiba MP, Hamna Amjad, Mohammed Farzin MP

## License
MIT. See the LICENSE file.
