import React, { useEffect, useState } from "react";
import { fetchTranscript } from "../api";

function TranscriptBox({ lead }) {
  const [data, setData] = useState(null);

  const load = async () => {
    try {
      const res = await fetchTranscript(lead.id);
      setData(res.data);
    } catch (e) {
      setData(null);
    }
  };

  useEffect(() => {
    load();
    const id = setInterval(load, 5000); // poll every 5s
    return () => clearInterval(id);
  }, [lead]);

  return (
    <div className="bg-white shadow rounded p-4">
      <h2 className="text-xl font-semibold mb-2">
        Transcript & Score for {lead.name}
      </h2>
      {data ? (
        <>
          <p className="whitespace-pre-wrap mb-2">{data.transcript}</p>
          <p className="font-bold">
            Lead Score:{" "}
            <span
              className={
                data.score > 70
                  ? "text-green-600"
                  : data.score > 40
                  ? "text-yellow-600"
                  : "text-red-600"
              }
            >
              {data.score}
            </span>
          </p>
        </>
      ) : (
        <p>No transcript yet. Wait for call completion.</p>
      )}
    </div>
  );
}

export default TranscriptBox;
