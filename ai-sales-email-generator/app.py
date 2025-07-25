# AI Sales Email Generator using LangChain + Streamlit

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os

# Load API key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Streamlit UI
st.title("✉️ AI Sales Email Generator")
st.markdown("Generate cold emails tailored to your product and audience 🎯")

# Inputs
product = st.text_input("Enter your product or service")
audience = st.text_input("Enter your target audience")
tone = st.selectbox("Select email tone", ["Professional", "Friendly", "Bold", "Persuasive"])

# Prompt Template
email_prompt = PromptTemplate(
    input_variables=["product", "audience", "tone"],
    template="""
You are a world-class sales copywriter. Write a cold email to pitch the product "{product}" to a target audience of "{audience}". Use a "{tone}" tone. 
Make sure it is:
- Short and engaging
- Has a strong hook
- Includes a call-to-action
    """
)

# LLM
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
chain = LLMChain(llm=llm, prompt=email_prompt)

# Generate Email
if st.button("Generate Email"):
    if product and audience:
        with st.spinner("Crafting your email..."):
            response = chain.run({"product": product, "audience": audience, "tone": tone})
            st.subheader("📧 Your AI-Generated Email")
            st.write(response)
    else:
        st.error("Please fill in both product and audience fields.")
