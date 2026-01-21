import streamlit as st
import google.generativeai as genai

# 1. Page Configuration & Branding
st.set_page_config(page_title="GuardianDev AI", page_icon="🛡️")
st.title("🛡️ GuardianDev AI")
st.markdown("### *Building the Future of Autonomous Security*")

# 2. Sidebar for API Key (Keep it flexible for now)
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your key at: aistudio.google.com")

if api_key:
    genai.configure(api_key=api_key)
    # Using Gemini 1.5 Flash for speed and cost-efficiency
    model = genai.GenerativeModel('gemini-1.5-flash')

    # 3. User Input Section
    st.divider()
    user_code = st.text_area("Paste your code here to scan for loopholes:", height=300)

    if st.button("Audit & Correct Code"):
        if user_code:
            with st.spinner("GuardianDev is analyzing..."):
                # 4. Our Specialized System Prompt
                prompt = f"""
                You are GuardianDev AI, a world-class Senior Security Engineer. 
                Perform the following:
                1. ANALYZE: Identify every security loophole and potential bug in this code.
                2. EXPLAIN: Tell the user why these vulnerabilities are dangerous in a professional way.
                3. REWRITE: Provide the FULL, corrected, and secure version of this code. 
                
                Input Code:
                {user_code}
                """
                response = model.generate_content(prompt)
                
                # 5. Displaying Results
                st.success("Analysis Complete!")
                st.markdown(response.text)
        else:
            st.error("Please provide code to audit.")
else:
    st.warning("👈 Please enter your Gemini API Key in the sidebar to activate GuardianDev.")
  
