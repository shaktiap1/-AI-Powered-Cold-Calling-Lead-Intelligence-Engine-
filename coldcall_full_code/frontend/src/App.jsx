import React, { useEffect, useState } from "react";
import LeadForm from "./components/LeadForm";
import CallButton from "./components/CallButton";
import TranscriptBox from "./components/TranscriptBox";
import { fetchLeads } from "./api";

function App() {
  const [leads, setLeads] = useState([]);
  const [selected, setSelected] = useState(null);

  const refresh = async () => {
    const { data } = await fetchLeads();
    setLeads(data);
  };

  useEffect(() => {
    refresh();
  }, []);

  return (
    <div className="max-w-4xl mx-auto p-4 space-y-6">
      <h1 className="text-3xl font-bold text-center">Cold Call AI</h1>
      <LeadForm onCreated={refresh} />

      <div className="bg-white shadow rounded p-4">
        <h2 className="text-xl font-semibold mb-2">Leads</h2>
        <ul>
          {leads.map((lead) => (
            <li
              key={lead.id}
              className={`p-2 border-b flex justify-between ${
                selected?.id === lead.id ? "bg-gray-100" : ""
              }`}
              onClick={() => setSelected(lead)}
            >
              <span>
                {lead.name} — {lead.company}
              </span>
              <CallButton lead={lead} />
            </li>
          ))}
        </ul>
      </div>

      {selected && <TranscriptBox lead={selected} />}
    </div>
  );
}

export default App;
