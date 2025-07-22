from .groq_caller import generate_script  # reuse for scoring prompt
import re

def score_lead(transcript: str) -> int:
    """Very naive lead scoring: count positive keywords."""
    positive = len(re.findall(r"\bgood|yes|sure|interested|great\b", transcript.lower()))
    negative = len(re.findall(r"\bno|not interested|busy|later\b", transcript.lower()))
    score = max(0, 50 + (positive - negative) * 10)  # range-ish 0–100
    return min(score, 100)
