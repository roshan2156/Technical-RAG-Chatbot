import streamlit as st
import requests

# ==========================================================
# Configuration
# ==========================================================

API_URL = "https://technical-rag-chatbot-1.onrender.com/query"

st.set_page_config(
    page_title="Technical RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Technical RAG Chatbot")
st.write("Ask technical questions about the indexed documentation.")

# ==========================================================
# User Input
# ==========================================================

question = st.text_input(
    "Enter your question",
    placeholder="Example: What is FastAPI?"
)

# ==========================================================
# Query Button
# ==========================================================

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Searching documentation..."):

            try:

                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=60
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Answer")
                    st.markdown(result.get("answer", "No answer returned."))

                else:

                    st.error(f"API Error: {response.status_code}")
                    st.write(response.text)

            except Exception as e:

                st.error(f"Connection Error: {e}")
