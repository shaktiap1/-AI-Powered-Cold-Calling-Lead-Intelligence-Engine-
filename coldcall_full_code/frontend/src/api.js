import axios from "axios";

const API = axios.create({ baseURL: "http://localhost:8001/api" });

// Lead endpoints
export const fetchLeads = () => API.get("/lead/");
export const createLead = (lead) => API.post("/lead/", lead);

// Call endpoints
export const startCall = (lead_id) => API.post("/call/start", { lead_id });

export const fetchTranscript = (lead_id) =>
  API.get(`/call/transcript/${lead_id}`);
