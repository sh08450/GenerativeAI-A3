from llm import calling_llm
# print(calling_llm("What is the capital of France?"))

# --- Part 1: Code → Security Fixes ---
code_snippets = [
    """
import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    return cursor.fetchall()
""",
    """
def connect_to_db():
    password = "admin123"  # Hardcoded password
    db = connect(host="localhost", user="admin", password=password)
    return db
""",
    """
def read_file(filename):
    with open(f"/uploads/{filename}", 'r') as f:
        return f.read()
"""
]

print("=== Part 1: Code Security Analysis ===")
for i, snippet in enumerate(code_snippets, 1):
    print(f"\n--- Test case {i} ---")
    response = calling_llm(f"Find security vulnerabilities in this code and recommend fixes. Focus ONLY on security issues, not general refactoring:\n\n{snippet}")
    print(response)

print("\n--------------------------------\n")

# --- Part 2: Specs → Potential Vulnerabilities ---
app_specs_list = [
    """
We are building an AI customer support chatbot that:
- Takes customer queries via chat interface
- Uses GPT-4 to generate responses
- Can access customer database to pull order history
- Allows customers to upload receipts/images
- Stores all conversations for training improvement
- Has a plugin system for third-party integrations
""",
    """
We are developing an AI coding assistant that:
- Accepts code snippets from developers
- Generates code suggestions using LLM
- Has access to the company's private codebase
- Can execute code in sandboxed environments
- Learns from user feedback to improve suggestions
- Integrates with GitHub and GitLab
"""
]

print("=== Part 2: App Specs Vulnerability Analysis ===")
for i, specs in enumerate(app_specs_list, 1):
    print(f"\n--- App Specs {i} ---")
    response = calling_llm(f"Based on these app specs, list potential security vulnerabilities mapped to OWASP Top 10 for LLM apps AND MITRE ATLAS perspective. Be specific,concise and actionable:\n\n{specs}")
    print(response)