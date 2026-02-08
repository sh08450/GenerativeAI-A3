#streamlit app
import streamlit as st
from llm import calling_llm

st.set_page_config(page_title="LLM Security Helper", layout="wide")
st.title("LLM Security Helper App")

tab1,tab2=st.tabs(["Code Security Analysis", "App Specs Vulnerability Analysis"])

#part 1: code->security analysis
with tab1:
    st.markdown("### Paste your code snippet for security analysis")
    code_input=st.text_area("Enter your code snippet here:")

    if st.button("Analyze Code Vulnerabilities"):
        if code_input.strip(): #check if the input is not empty
            with st.spinner("Analyzing code for vulnerabilities..."):
                response=calling_llm(f"Find security vulnerabilities in this code and recommend fixes. Focus ONLY on security issues, not general refactoring:\n\n{code_input}")
            with st.expander("LLM Analysis"):
                st.code(response, language="text")

#part 2: specs->potential vulnerabilities
with tab2:
    spec_input=st.text_area("Enter your SPECS here:")
    if st.button("Analyze Specs for Potential Vulnerabilities"):
        with st.spinner("Analyzing app specs for potential vulnerabilities..."):
            response=calling_llm(f"Based on these app specs, list potential security vulnerabilities mapped to OWASP Top 10 for LLM apps AND MITRE ATLAS perspective. Be specific,concise and actionable:\n\n{spec_input}")
        with st.expander("LLM Analysis"):
            st.code(response, language="text")

