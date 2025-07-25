import streamlit as st

# Set page title
st.set_page_config(page_title="Name List & Lengths", layout="centered")

# List of names
names = ["Ameena", "Elon", "Zara", "Alexander", "Nina"]

# Show heading
st.title("🧾 Name List with Lengths")

# Create table
name_data = [{"Name": name, "Length": len(name)} for name in names]

# Display as table
st.table(name_data)
