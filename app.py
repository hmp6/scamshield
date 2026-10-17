import streamlit as st
from rules import run_rules
from gemma import analyze

st.set_page_config(page_title="ScamShield", page_icon="🛡️")
st.title("🛡️ ScamShield")
st.write("Upload a suspicious message screenshot or paste the text. We'll tell you if it's a scam.")

language = st.selectbox("Answer language", ["English", "Hindi", "Malayalam"])
uploaded = st.file_uploader("Upload screenshot", type=["png", "jpg", "jpeg"])
text = st.text_area("Or paste the message text")

if st.button("Check message"):
    if not uploaded and not text.strip():
        st.warning("Please upload a screenshot or paste text.")
    else:
        image_bytes = uploaded.read() if uploaded else None
        with st.spinner("Analyzing..."):
            findings = run_rules(text)
            result = analyze(image_bytes, text, findings, language)

        verdict = result.get("verdict", "Suspicious")
        if verdict == "Scam":
            st.error(f"🚨 {verdict}")
        elif verdict == "Suspicious":
            st.warning(f"⚠️ {verdict}")
        else:
            st.success(f"✅ {verdict}")

        st.subheader("Why")
        for r in result.get("reasons", []):
            st.write("• " + r)

        st.subheader("What to do")
        for s in result.get("next_steps", []):
            st.write("• " + s)

        if findings:
            with st.expander("Automatic checks that fired"):
                for f in findings:
                    st.write("• " + f)

        st.caption("This is guidance, not a guarantee. When in doubt, don't pay or click.")