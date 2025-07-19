import requests

def enrich_lead(name, company):
    enriched_info = {
        'name': name,
        'company': company,
        'title': 'Software Engineer',
        'linkedin': f'https://linkedin.com/in/{name.lower()}',
        'tech_stack': ['Python', 'Flask', 'LLM']
    }
    return enriched_info
