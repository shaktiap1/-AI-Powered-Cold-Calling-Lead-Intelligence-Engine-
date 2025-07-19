def generate_call_script(lead_info):
    return (f"Hello {lead_info['name']}, this is an AI assistant reaching out regarding opportunities with "
            f"{lead_info['company']}. Based on your LinkedIn profile, we see you work with {', '.join(lead_info['tech_stack'])}. "
            "We'd love to connect. Thank you!")
