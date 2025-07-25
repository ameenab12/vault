# SimplePassword.py

import streamlit as st
import re

# Configuration
MIN_LENGTH = 8

# Streamlit App
st.title("🔐 Smart Password Strength Checker")

# Toggle for hiding/showing password
show_password = st.toggle("👁 Show password")

# Password input field
password = st.text_input("Enter your password:", type="default" if show_password else "password")

# Real-time feedback
if password:
    st.write("🔎 **Checking your password...**")

    # Rule checks
    checks = {
        "Minimum length (8 chars)": len(password) >= MIN_LENGTH,
        "At least one uppercase letter": bool(re.search(r'[A-Z]', password)),
        "At least one number": bool(re.search(r'\d', password)),
        "At least one special character (!@#$%^&*)": bool(re.search(r'[!@#$%^&*]', password))
    }

    # Display results
    passed = 0
    for rule, result in checks.items():
        if result:
            st.success(f"✅ {rule}")
            passed += 1
        else:
            st.error(f"❌ {rule}")

    # Final summary
    if passed == len(checks):
        st.balloons()
        st.markdown("🎉 **Strong password! Ready to go.**")
    else:
        st.markdown("🔐 **Keep refining your password for better security.**")

else:
    st.info("👈 Start typing your password to check its strength.")
