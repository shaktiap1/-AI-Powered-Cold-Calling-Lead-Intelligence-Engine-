import os, time, requests

AAI_KEY = os.getenv("ASSEMBLYAI_API_KEY", "your_assemblyai_key")
HEADERS = { "authorization": AAI_KEY }

def upload_audio(audio_url: str) -> str:
    """AssemblyAI can fetch from a public URL directly."""
    # No upload needed if Twilio recording is already publicly accessible
    return audio_url

def transcribe(audio_url: str) -> str:
    endpoint = "https://api.assemblyai.com/v2/transcript"
    resp = requests.post(endpoint, headers=HEADERS, json={ "audio_url": audio_url })
    resp.raise_for_status()
    transcript_id = resp.json()["id"]

    # Poll (simplified)
    status = "queued"
    while status not in ("completed", "error"):
        poll = requests.get(f"{endpoint}/{transcript_id}", headers=HEADERS)
        poll.raise_for_status()
        data = poll.json()
        status = data["status"]
        if status == "completed":
            return data["text"]
        elif status == "error":
            raise RuntimeError(data["error"])
        time.sleep(3)
