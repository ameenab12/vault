# CountNumbers.py

import streamlit as st

st.title("🔢 Count Positives, Negatives & Zeros")

user_input = st.text_input("Enter numbers separated by commas:", "3, -1, 0, 5, -9, 0, 4, -2")

try:
    numbers = [int(x.strip()) for x in user_input.split(",")]

    positives = sum(1 for n in numbers if n > 0)
    negatives = sum(1 for n in numbers if n < 0)
    zeros = sum(1 for n in numbers if n == 0)

    st.write(f"✅ Total numbers: {len(numbers)}")
    st.success(f"🔵 Positive numbers: {positives}")
    st.error(f"🔴 Negative numbers: {negatives}")
    st.info(f"⚫ Zeros: {zeros}")

except ValueError:
    st.warning("⚠️ Please enter only valid integers separated by commas.")
