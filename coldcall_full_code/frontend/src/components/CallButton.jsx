import React, { useState } from "react";
import { startCall } from "../api";

function CallButton({ lead }) {
  const [loading, setLoading] = useState(false);
  const handleClick = async () => {
    setLoading(true);
    await startCall(lead.id);
    setLoading(false);
    alert("Call initiated! Check your Twilio dashboard.");
  };
  return (
    <button
      onClick={handleClick}
      disabled={loading}
      className="px-3 py-1 bg-blue-600 text-white rounded"
    >
      {loading ? "Calling..." : "Call"}
    </button>
  );
}

export default CallButton;
