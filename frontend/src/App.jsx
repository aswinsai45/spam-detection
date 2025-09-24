import { useState } from "react";
import Hero from "./components/Hero";
import "./App.css";
function App() {
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleCheck = async (message) => {
    setLoading(true);
    setError("");
    setResult("");

    try {
      const response = await fetch(
        "https://spam-detection-nu9e.onrender.com/predict",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message }),
        }
      );

      if (!response.ok) throw new Error("Backend error");

      const data = await response.json();
      setResult(data.prediction);
    } catch (err) {
      setError("Could not connect to server");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Hero
      onSubmit={handleCheck}
      result={result}
      loading={loading}
      error={error}
    />
  );
}

export default App;
