def test_enrich_lead():
    from app.lead_enrichment import enrich_lead
    data = enrich_lead("Shaktesh", "Caprae")
    assert data['name'] == "Shaktesh"
    assert data['company'] == "Caprae"
