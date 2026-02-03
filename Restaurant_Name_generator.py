import streamlit as st
import google.generativeai as genai
import os
os.environ["GEMINI_API_KEY"] ="sk-----------"
# Configure page
st.set_page_config(
    page_title="🍽️ Restaurant Name Generator",
    page_icon="🍔",
    layout="centered"
)

# Load API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Title & description
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>🍽️ Restaurant Name Generator</h1>
    <p style='text-align: center; font-size:18px;'>
    Generate creative restaurant names using <b>Google Gemini AI</b>
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# User inputs
cuisine = st.text_input("🍕 Enter Cuisine Type", placeholder="e.g. Mexican, Indian, Italian")
style = st.selectbox(
    "🎨 Select Restaurant Style",
    ["Casual", "Luxury", "Modern", "Traditional", "Cafe Style"]
)

generate_btn = st.button("✨ Generate Restaurant Name")

# Gemini function
def generate_restaurant_name(cuisine, style):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    Suggest 5 creative and fancy restaurant names for a {style} style restaurant
    that serves {cuisine} food.
    """
    response = model.generate_content(prompt)
    return response.text

# Output
if generate_btn:
    if cuisine.strip() == "":
        st.warning("⚠️ Please enter a cuisine type.")
    else:
        with st.spinner("🍳 Cooking up some names..."):
            result = generate_restaurant_name(cuisine, style)

        st.success("🎉 Here are some name ideas:")
        st.markdown(
            f"""
            <div style="background-color:#F2F4F4; padding:15px; border-radius:10px;">
            <pre style="font-size:16px;">{result}</pre>
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()
st.caption("Built with ❤️ using Streamlit & Gemini API")
