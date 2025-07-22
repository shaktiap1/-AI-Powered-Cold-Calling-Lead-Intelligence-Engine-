import React, { useState } from "react";
import { createLead } from "../api";

function LeadForm({ onCreated }) {
  const [lead, setLead] = useState({
    name: "",
    phone: "",
    company: "",
    pain_point: ""
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createLead(lead);
    setLead({ name: "", phone: "", company: "", pain_point: "" });
    onCreated();
  };

  const handleChange = (e) =>
    setLead({ ...lead, [e.target.name]: e.target.value });

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white shadow rounded p-4 space-y-4"
    >
      <h2 className="text-xl font-semibold">Add Lead</h2>
      <div className="grid grid-cols-2 gap-4">
        <input
          className="border p-2 rounded"
          placeholder="Name"
          name="name"
          value={lead.name}
          onChange={handleChange}
          required
        />
        <input
          className="border p-2 rounded"
          placeholder="Phone (+1234567890)"
          name="phone"
          value={lead.phone}
          onChange={handleChange}
          required
        />
        <input
          className="border p-2 rounded col-span-2"
          placeholder="Company"
          name="company"
          value={lead.company}
          onChange={handleChange}
        />
        <input
          className="border p-2 rounded col-span-2"
          placeholder="Pain Point"
          name="pain_point"
          value={lead.pain_point}
          onChange={handleChange}
        />
      </div>
      <button className="px-4 py-2 bg-green-600 text-white rounded">
        Create Lead
      </button>
    </form>
  );
}

export default LeadForm;
