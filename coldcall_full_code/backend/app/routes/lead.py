import uuid
from flask import Blueprint, request, jsonify

leads = {}  # {id: {name, phone, company, pain_point}}

bp = Blueprint("lead", __name__, url_prefix="/api/lead")

@bp.route("/", methods=["GET"])
def list_leads():
    return jsonify(list(leads.values()))

@bp.route("/", methods=["POST"])
def add_lead():
    data = request.get_json(force=True)
    lead_id = uuid.uuid4().hex
    data["id"] = lead_id
    leads[lead_id] = data
    return jsonify(data), 201

@bp.route("/<lead_id>", methods=["GET"])
def get_lead(lead_id):
    lead = leads.get(lead_id)
    if not lead:
        return jsonify({"error": "Lead not found"}), 404
    return jsonify(lead)
