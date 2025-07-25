import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# LLM setupll
llm = ChatOpenAI(
    temperature=0.8,
    model_name="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Prompt template
journal_prompt = PromptTemplate(
    input_variables=["entry"],
    template="""
You are a kind, empathetic therapist and emotional coach.

A user has written this journal entry: 
"{entry}"

Respond with:
- Emotional reflection
- A positive, kind tone
- One reflective question to help them explore deeper
"""
)

chain = LLMChain(llm=llm, prompt=journal_prompt)

# UI
st.title("🧘‍♀️ AI Mood Journal")
st.markdown("Type how you're feeling and receive a thoughtful, kind reflection.")

entry = st.text_area("📝 Your Mood Journal", height=200)

if st.button("Reflect"):
    if entry.strip():
        with st.spinner("Thinking deeply..."):
            response = chain.run(entry)
            st.markdown("### 💬 AI Reflection")
            st.write(response)
    else:
        st.error("Please write something in your journal entry.")

st.markdown("---")
st.caption("Built with ❤️ using LangChain + Streamlit")
