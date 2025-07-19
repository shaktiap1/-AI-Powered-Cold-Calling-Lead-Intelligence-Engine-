from flask import Blueprint, render_template, request
from app.lead_enrichment import enrich_lead
from app.cold_calling import make_cold_call

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        company = request.form['company']
        phone = request.form['phone']

        enriched_data = enrich_lead(name, company)
        call_status = make_cold_call(phone, enriched_data)

        return render_template('result.html', data=enriched_data, status=call_status)

    return render_template('index.html')
