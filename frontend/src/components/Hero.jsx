import { useState } from "react";

export default function Hero({ onSubmit, result, loading, error }) {
  const [message, setMessage] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim()) {
      onSubmit(message);
      setMessage("");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-blue-100 via-white to-purple-200">
      <div className="backdrop-blur-2xl bg-white/70 shadow-2xl border border-blue-100 rounded-3xl px-10 py-12 w-full max-w-md transition-all duration-200">
        <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-700 via-purple-700 to-indigo-500 mb-8 text-center drop-shadow-md">
          📩 Spam Detector
        </h1>
        <form onSubmit={handleSubmit} className="flex flex-col gap-5">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your message here…"
            className="p-3 rounded-xl border border-gray-200 focus:border-blue-400 focus:ring-2 focus:ring-blue-100 transition-colors duration-200 shadow-sm placeholder-gray-400"
            autoFocus
            disabled={loading}
          />
          <button
            type="submit"
            disabled={loading}
            className={`py-3 rounded-xl font-bold shadow-lg transition-all duration-200 outline-none ${
              loading
                ? "bg-gray-300 text-gray-500 cursor-not-allowed"
                : "bg-gradient-to-r from-blue-500 to-purple-500 hover:from-blue-600 hover:to-purple-600 text-white"
            }`}
          >
            {loading ? "Checking..." : "Check"}
          </button>

          {/* Feedback */}
          <div className="h-14">
            {loading && (
              <div className="p-3 rounded-xl text-center text-blue-500 font-semibold animate-pulse">
                Analyzing message...
              </div>
            )}

            {error && (
              <div className="p-3 rounded-xl text-center bg-red-50 text-red-600 font-bold border border-red-200 shadow">
                ⚠️ {error}
              </div>
            )}

            {!loading && result && (
              <div
                className={`p-3 rounded-xl text-center text-lg font-semibold border shadow transition-all duration-200 ${
                  result === "spam"
                    ? "bg-red-100 text-red-600 border-red-300"
                    : "bg-green-100 text-green-600 border-green-300"
                }`}
              >
                {result === "spam" ? "🚨 Spam Detected!" : "✅ Not Spam"}
              </div>
            )}
          </div>
        </form>
      </div>
      <div className="mt-10 text-sm text-gray-400">
        <span className="italic">Powered by AI · Built with Tailwind CSS</span>
      </div>
    </div>
  );
}
