#streamlit app
import streamlit as st
from llm import calling_llm

st.title("LLM Security Helper App")

tab1,tab2=st.tabs(["Part1: Code->Security Analysis","Part2: Specs->Potential Vulnerabilities"])

#part 1: code->security analysis
with tab1:
    code_input=st.text_area("Enter your code snippet here:")
    if st.button("Analyze Code Vulnerabilities"):
        if code_input.strip(): #check if the input is not empty
            response=calling_llm(f"Find security vulnerabilities in this code and recommend fixes. Focus ONLY on security issues, not general refactoring:\n\n{code_input}")
            st.subheader("LLM's Analysis:")
            st.write(response) 

#part 2: specs->potential vulnerabilities
with tab2:
    spec_input=st.text_area("Enter your SPECS here:")
    if st.button("Analyze Specs for Potential Vulnerabilities"):
        if spec_input:
            response=calling_llm(f"Based on these app specs, list potential security vulnerabilities mapped to OWASP Top 10 for LLM apps AND MITRE ATLAS perspective. Be specific,concise and actionable:\n\n{spec_input}")
            st.subheader("LLM's Analysis:")
            st.write(response)
