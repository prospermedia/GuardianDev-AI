import streamlit as st
import google.generativeai as genai
import time

# 1. Page Configuration & Branding
st.set_page_config(page_title="GuardianDev AI", page_icon="🛡️")
st.title("🛡️ GuardianDev AI")
st.markdown("### *Autonomous Security & Code Correction*")

# 2. Sidebar Settings
with st.sidebar:
    st.title("🛡️ Dashboard")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Built by Prosper | Future of Security")
    st.divider()
    st.markdown("**.LOGS**")
    st.caption("v2.0: Added RCE & SQLi specialized detection.")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')

        # 3. User Input Section
        user_code = st.text_area("Paste code here to hunt for loopholes:", height=250)

        if st.button("Audit & Correct Code"):
            if user_code:
                # The Loading Spinner
                with st.spinner("🛡️ GuardianDev is analyzing for loopholes..."):
                    try:
                        # Tiny delay to help prevent rate-limit crashes
                        time.sleep(1) 
                        
                        prompt = f"""
                        You are GuardianDev AI, a Senior Security Engineer. 
                        1. ANALYZE: Identify every security loophole in this code.
                        2. EXPLAIN: Why it is dangerous.
                        3. REWRITE: Provide the FULL, corrected, and secure code.
                        
                        Code:
                        {user_code}
                        """
                        response = model.generate_content(prompt)
                        
                        st.success("Audit Complete!")
                        st.markdown(response.text)
                        
                        # Professional cooldown reminder
                        st.warning("🕒 System cooling down. Please wait 30s before next audit.")
                        
                    except Exception as e:
                        if "ResourceExhausted" in str(e):
                            st.error("⚠️ Server Busy: Google's free tier is resting. Wait 1 minute and try again.")
                        else:
                            st.error(f"Error: {e}")
            else:
                st.warning("Please paste code first!")
    except Exception as init_error:
        st.error(f"Configuration Error: {init_error}")
else:
    st.warning("👈 Please enter your API Key in the sidebar to start.")

# 4. The "Expert" Footer (Builds your brand)
st.divider()
st.markdown("#### 💡 Security Tip of the Day")
st.caption("Never use `eval()` or `exec()` with user-provided input. It allows 'Remote Code Execution' (RCE), giving hackers full control of your server.")
