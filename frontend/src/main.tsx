import React from "react";
import { createRoot } from "react-dom/client";

function App() {
  return <main><h1>AI Team Starter</h1><p>Connect this frontend to POST /api/v1/chat.</p></main>;
}

createRoot(document.getElementById("root")!).render(<App />);

