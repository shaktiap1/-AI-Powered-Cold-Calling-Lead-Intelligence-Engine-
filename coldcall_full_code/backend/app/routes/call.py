import os, uuid, requests
from flask import Blueprint, request, Response, jsonify
from twilio.twiml.voice_response import VoiceResponse
from app.services.twilio_client import make_call
from app.services.groq_caller import generate_script
from app.services.lead_scoring import score_lead
from app.services.assemblyai_client import transcribe

from .lead import leads  # import the in‑memory store

bp = Blueprint("call", __name__, url_prefix="/api/call")
transcripts = {}  # {lead_id: transcript_text}

@bp.route("/start", methods=["POST"])
def start_call():
    data = request.get_json(force=True)
    lead_id = data.get("lead_id")
    lead = leads.get(lead_id)
    if not lead:
        return jsonify({"error": "Lead not found"}), 404

    call_sid = make_call(lead["phone"], lead_id)
    return jsonify({"call_sid": call_sid})

@bp.route("/voice", methods=["POST", "GET"])
def voice():
    lead_id = request.args.get("lead_id")
    lead = leads.get(lead_id, {})
    script = generate_script(lead)

    vr = VoiceResponse()
    vr.say(script, voice="man", language="en-US")
    vr.record(max_length=120, play_beep=True)
    return Response(str(vr), mimetype="text/xml")

@bp.route("/status", methods=["POST"])
def status_callback():
    # Twilio posts call status updates here
    return ("", 204)

@bp.route("/recording", methods=["POST"])
def recording():
    # Twilio posts RecordingUrl after call
    recording_url = request.form.get("RecordingUrl")
    lead_id = request.args.get("lead_id") or request.form.get("lead_id")
    if recording_url and lead_id:
        transcript = transcribe(recording_url + ".mp3")
        transcripts[lead_id] = {
            "transcript": transcript,
            "score": score_lead(transcript)
        }
    return ("", 204)

@bp.route("/transcript/<lead_id>", methods=["GET"])
def get_transcript(lead_id):
    data = transcripts.get(lead_id)
    if not data:
        return jsonify({"error": "Transcript not found"}), 404
    return jsonify(data)
