import os, requests, json

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your_groq_key")
ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def generate_script(lead_info: dict) -> str:
    system_prompt = "You are an expert sales rep. Generate a concise yet persuasive cold call script."
    user_prompt = f"""Lead details:
    Name: {lead_info.get('name')}
    Company: {lead_info.get('company')}
    Pain Point: {lead_info.get('pain_point', 'N/A')}

    Script:"""
    body = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.7
    }
    resp = requests.post(ENDPOINT, headers=HEADERS, json=body, timeout=60)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()
